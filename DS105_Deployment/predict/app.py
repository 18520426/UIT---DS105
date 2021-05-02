import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import random
from fbprophet import Prophet
from datetime import datetime

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    #date = datetime.strptime(request.form.values, '%Y-%m-%d').date()
    future = model.make_future_dataframe(periods=7)
    prediction = model.predict(future)
    seed = random.randint(0,len(future))

    return render_template('index.html', prediction_text=f'Case on {forecast.iloc[seed,0]} is about {forecast.iloc[seed,-1]}')

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)