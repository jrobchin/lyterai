from .preprocessors import ImagePreprocessor

def preprocess(model, data):
    """ 
    model: object representation of the db model
    data: list of data
    input_shape: (dimx, dimy)
    """

    framework = model.framework
    data_type = model.data_type
    dimensions = model.dimension_set.filter(dtype='input')

    # Build appropriate preprocessor
    if data_type == 'image path':
        preprocessor = ImagePreprocessor(model, dimensions.get(dimension='x'), dimensions.get(dimension='y'))
    else:
        raise NotImplementedError("{} for {} not implemented".format(data_type, framework))

    output, demo_id = preprocessor.preprocess(data)

    # Return processed data
    return output, demo_id