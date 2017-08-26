from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import MLModel, Layer, Example

def index(request):
	# Query all available models
	models = MLModel.objects.all()

	return render(request, 'hub/index.html', {'models': models})

def show(request, slug):
	context = {}
	# Get requested model
	model = get_object_or_404(MLModel, slug=slug)

	return render(request, 'hub/show.html', {'model': model})