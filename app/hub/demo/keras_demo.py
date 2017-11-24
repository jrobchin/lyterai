from keras import backend as K
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from keras.models import model_from_json
K.set_image_dim_ordering('tf')
K.set_image_data_format('channels_last')

def load_model(layers, weights):
    # Load model architecture and parameters
    model_json = open(layers, 'r')
    loaded_model_json = model_json.read()
    model_json.close()
    model = model_from_json(loaded_model_json)

    # Load model weights
    model.load_weights(weights)

    return model

def predict(image, layers, weights, classes_str):
    """
        Takes a path to an image and returns the predicted class and confidence score.
    """   

    classes = classes_str.split(",")

    K.clear_session()
    # Make and parse the prediction
    model = load_model(layers, weights)
    output = model.predict(image)
    prediction_index = output[0].argmax()
    confidence = float(output[0][prediction_index])
    # prediction = {'class': classes[prediction_index], 'confidence': confidence}
    prediction = classes[prediction_index]
    K.clear_session()

    return prediction, confidence