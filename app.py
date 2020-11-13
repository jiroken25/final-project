from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import model_from_json

def model_predict(x):
    model = model_from_json(open('covid_model.json', 'r').read())
    model.load_weights('covid_weights.h5')
    class_figure = model.predict_classes(np.array([x]),batch_size=1)[0]
    if class_figure == 1:
        output = "Successful"
    else:
        output =  "Failed"

    return output

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
       x = [float(request.form["health"]),float(request.form["bed"]),float(request.form["stay"]),float(request.form["life"]),float(request.form["unemployment"]),float(request.form["obesity"]),float(request.form["transport"]),float(request.form["poverty"]),float(request.form["science"])]
       output = model_predict(x)
       return render_template('predict.html',output=output)

    
if __name__ == '__main__':
	app.run()