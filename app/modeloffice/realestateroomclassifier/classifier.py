import os
import random
from urllib.parse import urlsplit
import requests
import numpy as np
import tensorflow as tf
from keras import backend as K
from keras.preprocessing import image as kimage
from keras.applications.imagenet_utils import preprocess_input
from keras.models import model_from_json
K.set_image_dim_ordering('tf')
K.set_image_data_format('channels_last')

MODEL_DIR = os.path.dirname(__file__)
MODEL_JSON_PATH = os.path.join(MODEL_DIR, 'model.json')
MODEL_WEIGHTS_PATH = os.path.join(MODEL_DIR, 'model.h5')

class RealEstateImageClassifier():
    def __init__(self):
        self.model_json_path = MODEL_JSON_PATH
        self.model_weights_path = MODEL_WEIGHTS_PATH
        self.classes = ['backyard', 'bathroom', 'bedroom', 'condo', 'house', 'kitchen', 'livingroom']
        self.model = self.load_model()
        self.graph = tf.get_default_graph()

    def load_model(self):
        # Load model architecture and parameters
        model_json = open(self.model_json_path, 'r')
        loaded_model_json = model_json.read()
        model_json.close()
        model = model_from_json(loaded_model_json)

        # Load model weights
        model.load_weights(self.model_weights_path)

        return model

    def preprocess(self, image_url):
        suffix_list = ['jpg', 'gif', 'png', 'tif', 'svg',]
        fname = image_url.strip("/").split("/")[-1].split(":")[-1]
        chars = 'abcdefghijklmnopqrxtuvwxyz'
        file_suffix = fname.split('.')[-1].lower()
        file_name = ''.join([chars[random.randint(0, len(chars)-1)] for x in range(10)]) + "." + file_suffix
        file_path = os.path.join(MODEL_DIR, "images", file_name)
        r = requests.get(image_url)
        print("Request", r)
        if file_suffix in suffix_list and r.status_code == requests.codes.ok:
            with open(file_path, 'wb+') as file:
                file.write(r.content)

            return file_path
        else:
            return False

    def predict(self, image_path=None, image_url=None):
        if image_path == None and image_url == None:
            raise TypeError("No image or image_url input.")
        if image_url != None:
            image_path = self.preprocess(image_url)

        try:
            img = kimage.load_img(image_path, target_size=(224, 224))
        except FileNotFoundError as e:
            return False

        img = kimage.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        image_processed = preprocess_input(img)

        output = []
        with self.graph.as_default():
            output = self.model.predict(image_processed)
        prediction_index = output[0].argmax()
        confidence = float(output[0][prediction_index])
        # prediction = {'class': classes[prediction_index], 'confidence': confidence}
        prediction = self.classes[prediction_index]

        os.remove(image_path)

        return prediction, confidence