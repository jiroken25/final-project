from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import model_from_json
from flask_sqlalchemy import SQLAlchemy
import json



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
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    result = db.session.execute('SELECT "Country","Population","Death","death/population","Health_Spending","Hospital_bed","Hospital_stay","Life_expectancy","Unemployment_rate","Obesity_rate","transporation","poverty_rate",	"science_score" FROM country_name inner join covid_data on country_name.index = covid_data.country_id inner join health_spending on country_name.index = health_spending.country_id inner join hospital_bed on country_name.index = hospital_bed.country_id inner join hospital_stay on country_name.index = hospital_stay.country_id inner join life_expectancy on country_name.index = life_expectancy.country_id inner join unemployment on country_name.index = unemployment.country_id inner join obesity on country_name.index = obesity.country_id inner join transporation on country_name.index = transporation.country_id inner join poverty on country_name.index = poverty.country_id inner join "Science_score" on country_name.index = "Science_score".country_id')
    data = json.dumps([dict(r) for r in result])
	
    return render_template('index.html',data=data)

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
       x = [float(request.form["health"]),float(request.form["bed"]),float(request.form["stay"]),float(request.form["life"]),float(request.form["unemployment"]),float(request.form["obesity"]),float(request.form["transport"]),float(request.form["poverty"]),float(request.form["science"])]
       output = model_predict(x)
       return render_template('predict.html',output=output)

    
if __name__ == '__main__':
	app.run()