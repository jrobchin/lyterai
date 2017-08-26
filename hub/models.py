import os

from django.db import models
from django.utils.text import slugify

from django.conf import settings

from positions import PositionField
from jsonfield import JSONField

from django.core.files.storage import FileSystemStorage

model_fs = FileSystemStorage(location=settings.MODEL_ROOT, base_url=settings.MODEL_URL)

def get_model_upload_to(instance, filename):
	return os.path.join(instance.slug, filename)

class MLModel(models.Model):
	prepopulated_fields = {"slug": ("title",)}
	name = models.CharField(max_length=200, unique=True)
	category = models.CharField(max_length=200)
	description = models.TextField(max_length=140)
	about = models.TextField(null=True, blank=True)
	slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
	model = models.FileField(upload_to=get_model_upload_to, storage=model_fs, null=True, blank=True)
	weights = models.FileField(upload_to=get_model_upload_to, storage=model_fs, null=True, blank=True)
	accuracy = models.FloatField()
	image = models.ImageField(upload_to='models/')
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(MLModel, self).save(*args, **kwargs)

	def __str__(self):
		return "{}: {}".format(self.name, self.category)

class Example(models.Model):
	ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
	position = PositionField(collection="ml_model")
	image = models.ImageField(upload_to='examples/')
	description = models.TextField(null=True, blank=True)
	source = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return "{} - Example {}".format(self.ml_model.name, self.position)

class Layer(models.Model):
	ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
	position = PositionField(collection="ml_model")
	name = models.CharField(max_length=100)
	layer_type = models.CharField(max_length=100, default="none")
	input_shape = models.CharField(max_length=50)
	output_shape = models.CharField(max_length=50)
	properties = JSONField(null=True, blank=True)

	def __str__(self):
		return "{}: {}".format(self.ml_model.name, self.name)