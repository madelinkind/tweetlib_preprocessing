import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

#Python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier

from pylab import rcParams

from imblearn.under_sampling import NearMiss
from imblearn.over_sampling import RandomOverSampler
from imblearn.combine import SMOTETomek
from imblearn.ensemble import BalancedBaggingClassifier

import os
import sys

FILE = __file__
DATA_SET_FOLDER = os.path.split(FILE)[0]
TWEET_LIB_FOLDER = os.path.split(DATA_SET_FOLDER)[0]
PROJECT_FOLDER = os.path.split(TWEET_LIB_FOLDER)[0]

sys.path.append(PROJECT_FOLDER)

from tweetlib.data_set.data_set import DataSet
from tweetlib.config.configuration import Configuration
from tweetlib.encoding import postagging
from tweetlib.definitions import TaggingMethod

class LogisticRegression(object):

    def __init__(self, config: Configuration, dataset: DataSet):
        super(TwitterPipeline, self).__init__()

        self.config = config
        self.dataset = dataset

    def run(self):
        # get data and classes from self.data
        data = self.dataset.get_data()
        y = self.dataset.get_y()
        vectors = []
        # for each preprocessing in self.config
            # apply preprocessing to data

        # apply encoding
        for text in data:
            v = postagging.postagging_encoding(text, TaggingMethod.SPACY)
            vectors.append(v)
        X = np.vstack(vectors)

        # classify
        #Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
        #dividimos en sets de entrenamiento y test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

        def run_model(X_train, X_test, y_train, y_test):
            clf = LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg")
            clf.fit(X_train, y_train)
            return clf
    
        #ejecutamos el modelo "tal cual"
        model = run_model(X_train, X_test, y_train, y_test)

        pred_y = model.predict(X_test)

        #definimos funciona para mostrar los resultados
        def mostrar_resultados(y_test, pred_y):
            conf_matrix = confusion_matrix(y_test, pred_y)
            plt.figure(figsize=(12, 12))
            LABELS= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
            plt.title("Confusion matrix")
            plt.ylabel('True class')
            plt.xlabel('Predicted class')
            plt.show()
            print (classification_report(y_test, pred_y))
        
        mostrar_resultados(y_test, pred_y)
