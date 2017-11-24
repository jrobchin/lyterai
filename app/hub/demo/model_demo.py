from hub.preprocessing import preprocess
from hub.models import MLModel, DemoResults
from . import keras_demo

def model_demo(model_id, data):
    # Get model data
    model = MLModel.objects.get(pk=model_id)

    # Preprocess data
    p_data, demo_id = preprocess.preprocess(model, data)
    
    # Make prediction
    if model.framework == 'keras':
        pred, conf = keras_demo.predict(p_data, model.model.path, model.weights.path, model.output_classes)
        DemoResults.objects.filter(pk=demo_id).update(prediction=pred, confidence=conf)
        return pred, conf

    return False