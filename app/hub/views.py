import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import MLModel, Layer, Example

from .demo import model_demo

def index(request):
	# Query all available models
	models = MLModel.objects.all()

	return render(request, 'hub/index.html', {'models': models})

def show(request, slug):
	context = {}
	# Get requested model
	model = get_object_or_404(MLModel, slug=slug)
	if model:
		layers = []
		# Get properties for each layer
		for layer in model.layer_set.all():
			# TODO: sort by key alphabetically or otherwise
			ps = []
			for key, value in layer.properties.items():
				k = key.replace("_", " ")
				ps.append("{}: {}".format(k.title(), value))

			layers.append({
				'id': 	layer.id,
				'name': layer.name,
				'type': layer.layer_type,
				'properties': ps
				# 'properties': json.loads(layer.properties.decode("utf-8"))
				# 'properties': layer.properties
			})

	return render(request, 'hub/show.html', {'model': model, 'layers': layers})

def demo(request):
	if request.POST:
		try:
			prediction, confidence = model_demo.model_demo(request.POST['model-id'], request.POST['data'])
		except Exception as e:
			raise(e)
		if prediction:
			return JsonResponse({'image-url': request.POST['data'],'prediction': prediction, 'confidence': confidence})
		else:
			return JsonResponse({'prediction': 'error', 'confidence': 'error'})
	else:
		return HttpResponse("Error: Cannot get demo.")
