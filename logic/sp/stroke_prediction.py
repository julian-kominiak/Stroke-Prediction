import pandas as pd
from flask import Flask, request, jsonify
from DataProcessing import DataProcessing
from Classificators import *

app = Flask(__name__)

@app.route("/analyse/sample_data", methods=['POST'])
def analyse_data():
    trainset = pd.read_csv('dataset.csv', index_col="Unnamed: 0")
    sample = pd.Series(data=request.get_json())

    BayesPrediction = NaiveBayes.classify(trainset, sample)
    KNNPrediction = KNN.clustering(sample, trainset, 3)
    StrokePrediction = (float(0.94) * float(BayesPrediction) + float(0.93) * float(KNNPrediction)) / 2
    probability = round(StrokePrediction * 100, 1)

    return jsonify(
        probablity=probability
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
