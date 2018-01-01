import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from django.db import models
from positions import PositionField
from jsonfield import JSONField

from .utils import model_parse

model_fs = FileSystemStorage(location=settings.MODEL_ROOT, base_url=settings.MODEL_URL)

def get_model_upload_to(instance, filename):
	return os.path.join(instance.slug, filename)

class MLModel(models.Model):
	prepopulated_fields = {"slug": ("title",)}

	name = models.CharField(max_length=200, unique=True)
	category = models.CharField(max_length=200)
	data_type = models.CharField(max_length=50, null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	about = models.TextField(max_length=2000)
	architecture = models.TextField(null=True, blank=True)
	slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
	demo = models.BooleanField(blank=True, default=False)
	sample = models.CharField(max_length=200, blank=True, null=True)
	output_classes = models.CharField(blank=True, max_length=1000)
	framework = models.CharField(max_length=50, null=True, blank=True)
	model = models.FileField(upload_to=get_model_upload_to, storage=model_fs, null=True, blank=True)
	weights = models.FileField(upload_to=get_model_upload_to, storage=model_fs, null=True, blank=True)
	accuracy = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to='models/')
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)

		if self.model:
			self.layer_set.all().delete()
			if self.model.readable():
				file_ext = self.model.name.split(".")[-1]
				file_contents = self.model.read()
				# LOGGING
				print("File ext: {}".format(file_ext))
				print("File contents: {}".format(file_contents))
				layers = model_parse.parse(file_contents, ext=file_ext, framework=self.framework)

				print("LAYERS: {}".format(layers))

				count = 0
				for layer in layers:
					Layer.objects.create(
						ml_model=self,
						position=count, 
						name=layer['name'], 
						layer_type=layer['type'],
						properties=layer['properties']
					)
					count+=1

		super(MLModel, self).save(*args, **kwargs)

	def __str__(self):
		return "{}: {}".format(self.name, self.category)

class Dimension(models.Model):
	ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
	dimension = models.CharField(max_length=1)
	value = models.IntegerField()
	dtype = models.CharField(max_length=100)

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
	properties = JSONField(null=True, blank=True)

	def __str__(self):
		return "{}: {}".format(self.ml_model.name, self.name)

class Preprocessor(models.Model):
	ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
	position = PositionField(collection='ml_model')
	ptype = models.CharField(max_length=100)

# For use in storing classifier outputs
class Classes(models.Model):
	ml_model = models.ForeignKey(MLModel, on_delete=models.CASCADE)
	position = PositionField(collection='ml_model') # index
	label = models.CharField(max_length=100)

class DemoResults(models.Model):
	ml_model = models.ForeignKey(MLModel)
	data = models.CharField(max_length=100, null=True, blank=True)
	file = models.FileField(upload_to='demos/', null=True, blank=True)
	prediction = models.CharField(max_length=100)
	confidence = models.FloatField(null=True, blank=True)

	def __str__(self):
		return "{} - {}: {}".format(self.pk, self.ml_model.name, self.data)