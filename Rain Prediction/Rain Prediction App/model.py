# model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np


class RainPredictor:
    def __init__(self):
        # Training data
        data = {
            'Temperature': [22, 25, 30, 35, 28, 18, 15, 20, 21, 29],
            'Humidity':    [80, 70, 60, 55, 65, 90, 95, 85, 88, 60],
            'Pressure':    [1012, 1010, 1005, 1003, 1008, 1015, 1018, 1013, 1011, 1006],
            'WindSpeed':   [5, 7, 10, 12, 8, 4, 3, 6, 5, 9],
            'Rain':        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
        }
        df = pd.DataFrame(data)
        X = df[['Temperature', 'Humidity', 'Pressure', 'WindSpeed']]
        y = df['Rain']

        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X, y)

    def predict(self, features: list) -> str:
        input_array = np.array(features).reshape(1, -1)
        prediction = self.model.predict(input_array)[0]
        return "Rain" if prediction == 1 else "No Rain"
