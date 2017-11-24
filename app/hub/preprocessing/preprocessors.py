import tempfile
from urllib.parse import urlsplit
import requests
import requests
import numpy as np
from keras.preprocessing import image as kimage
from keras.applications.imagenet_utils import preprocess_input
from django.core.files import File

from django.core.files.base import ContentFile

from hub.models import DemoResults

class ImagePreprocessor(object):
    """docstring for ImagePreprocessor"""
    def __init__(self, model, target_dim_x, target_dim_y):
        super(ImagePreprocessor, self).__init__()
        self.model = model
        self.framework = model.framework
        self.target_dim_x = target_dim_x.value
        self.target_dim_y = target_dim_y.value
        
    def request_image(self, file_url):
        try:
            # Check for existing demo
            d = DemoResults.objects.get(ml_model=model, data=file_url)
            return d.file.path, d.pk
        except:            
            suffix_list = ['jpg', 'gif', 'png', 'tif', 'svg',]
            file_name = urlsplit(file_url)[2].split('/')[-1].strip('/')
            file_suffix = file_name.split('.')[1].lower()
            r = requests.get(file_url)
            if file_suffix in suffix_list and r.status_code == requests.codes.ok:
                file = ContentFile(r.content, file_name)
                
                demo = DemoResults(ml_model=self.model)
                demo.data = file_url
                demo.file = file
                demo.save()

                file.close()

                path = demo.file.path
                demo.delete()

                return path, demo.pk

            else:
                return False

    def preprocess(self, image_url):
        # Download the photo
        image_path, demo_id = self.request_image(image_url)
        
        # Apply preprocessing
        if self.framework == 'keras':
            try:
                img = kimage.load_img(image_path, target_size=(self.target_dim_x, self.target_dim_y))
            except FileNotFoundError as e:
                return False

            img = kimage.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            image_processed = preprocess_input(img)

            return image_processed, demo_id
        else:
            raise NotImplementedError("{} has not been implemented".format(self.framework))