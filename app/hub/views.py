import json
import requests

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import MLModel, Layer, Example

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
			})

	return render(request, 'hub/show.html', {'model': model, 'layers': layers})

def demo(request):
	if request.POST:
		try:
			payload = {'image-url': request.POST['data']}
			url = "http://office:5000/realestateclassifier"
			response = requests.request("POST", url, data=payload)
			prediction = response.json()
		except Exception as e:
			return JsonResponse({'prediction': 'error', 'confidence': 'error'})
		if prediction:
			return JsonResponse({'image-url': request.POST['data'],'prediction': prediction['prediction'], 'confidence': prediction['confidence']})
		else:
			return JsonResponse({'prediction': 'none', 'confidence': 'none'})
	else:
		return HttpResponse("Error: Cannot get demo.")
