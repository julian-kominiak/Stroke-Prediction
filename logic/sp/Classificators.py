import pandas as pd
import numpy as np
import random as rd

class NaiveBayes:
    def __init__(self):
        return

    @staticmethod
    def gauss(x, mean, std):
        if std == 0.0:
            std = 0.0001
        exponent = np.exp(-(x-mean)**2/(2*std**2))
        return 1/(np.sqrt(2*np.pi*std**2))*exponent
    
    @staticmethod
    def classify(trainSet, sample):
        stroke = trainSet.query('stroke == 1')
        not_stroke = trainSet.query('stroke == 0')
        classes = [stroke,not_stroke]

        probabilities = []
        for c in classes:
            means = []
            stds = []
            for atr in c:
                means.append(c[atr].mean())
                stds.append(c[atr].std())
            
            prob = 1

            for i in range(10):
                prob *= NaiveBayes.gauss(sample[i],means[i],stds[i])
            probabilities.append(prob)

        for i in range(2):
            if probabilities[i] == max(probabilities):
                return classes[i]['stroke'].iloc[0]


class KNN:
    @staticmethod
    def minkowski_metric(v1,v2,m):
        distance = 0
        for i in range(len(v1)-1):
            distance+=(abs(v1[i]-v2[i])*m)
        distance = distance **(1/m)
        return distance
    @staticmethod
    def clustering(sample, x, k):
        distances = []
        classes = {'1.0': 0, '0.0': 0}
        for i in x.index:
            distances.append([KNN.minkowski_metric(sample, x.iloc[i], 2), x.iloc[i].stroke])
            
        distances = sorted(distances)
        for i in range(k):
            classes[str(distances[i][1])]+=1

        return max(classes, key=classes.get)