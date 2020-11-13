import numpy as np
from keras.models import model_from_json

def model_predict(x):
    model = model_from_json(open('covid_model.json', 'r').read())
    model.load_weights('covid_weights.h5')
    class_figure = model.predict_classes(np.array([x]),batch_size=1)[0]
    if class_figure == 1:
        output = "Successful"
    else:
        output =  "Failed"

    return output