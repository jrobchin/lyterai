import json

def parse(file_contents, ext, framework):
	if ext == "json":
		if framework == "keras":
			data = json.loads(file_contents.decode("utf-8"))

			layers = []
			for layer in data['config']['layers']:
				l = {}
				l['name'] = layer['name']
				l['type'] = layer['class_name']
				l['properties'] = layer['config']
				# TODO: add more processing for input/ouput shapes

				layers.append(l)

			return layers
