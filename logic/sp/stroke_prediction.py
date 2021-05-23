import pandas as pd
from flask import Flask, request, jsonify
from DataProcessing import DataProcessing
from Classificators import *

app = Flask(__name__)

print("Probability of stroke is:", round(StrokePrediction * 100, 1),"%")

@app.route("/analyse/sample_data", methods=['POST'])
def analyse_data():
    # sample_data = request.get_json()['sample_data']
    dataset = pd.read_csv('dataset.csv', index_col="Unnamed: 0")
    sample = pd.Series(data={'is_female': 0, 'age': 81, 'is_urban': 1, 'is_working': 0.75,
                            'hypertension': 0, 'heart_disease': 0, 'ever_married': 1,
                            'avg_glucose_level': 186.21, 'bmi': 29, 'smoking_status': 0.5})
    BayesPrediction = NaiveBayes.classify(dataset, sample)
    KNNPrediction = KNN.clustering(sample, dataset, 3)
    probability = (float(0.94) * float(BayesPrediction) + float(0.93) * float(KNNPrediction)) / 2
    return jsonify(
        probablity=probability
    )
    return
