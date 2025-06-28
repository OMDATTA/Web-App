# app.py
from flask import Flask, render_template, request
from model import RainPredictor
from utils import validate_inputs

app = Flask(__name__)
predictor = RainPredictor()


@app.route('/')
def index():
    return render_template('index.html', result=None)


@app.route('/predict', methods=['POST'])
def predict():
    form_data = {
        'Temperature': request.form.get('temperature'),
        'Humidity': request.form.get('humidity'),
        'Pressure': request.form.get('pressure'),
        'WindSpeed': request.form.get('windspeed')
    }

    is_valid, message = validate_inputs(form_data)
    if not is_valid:
        return render_template('index.html', result=f"Error: {message}")

    features = [float(val) for val in form_data.values()]
    result = predictor.predict(features)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
