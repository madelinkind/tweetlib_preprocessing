import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score
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
from tweetlib.definitions import TaggingMethod, ClassificationMethod
import models
from joblib import dump
# from tweetlib.pipeline.execute_pipeline import TwitterPipeline

class Classification(object):

    #Validate
    @staticmethod
    def validation_method(X, y, method: ClassificationMethod):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]
            method (ClassificationMethod): [description]
        """
        accuracy=[]
        kfold_list = []
       #Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
        #dividimos en sets de entrenamiento y test
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        y = np.array(y)
        skf = StratifiedKFold(n_splits=5, random_state=None)
        skf.get_n_splits(X,y)
        StratifiedKFold(n_splits=2, random_state=None, shuffle=False)
        for train_index, test_index in skf.split(X, y):
            # print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            #ejecutamos el modelo
            model = Classification.run_model_balanced(X_train, y_train, method)

            # se realiza las predicciones en los datos de prueba usando predict()
            pred_y = model.predict(X_test)
            # print(pred_y)
            score = accuracy_score(pred_y, y_test)
            accuracy.append(score)
            #mostrar los resultados
            conf_matrix = confusion_matrix(y_test, pred_y)
            plt.figure(figsize=(12, 12))
            #Cambios recientes, borrar comentario luego
            LABELS= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
            plt.title("Confusion matrix")
            plt.ylabel('True class')
            plt.xlabel('Predicted class')
            plt.show()
            print (classification_report(y_test, pred_y))
        accuracy_mean = np.array(accuracy).mean()
        print(f"Iter1_Accuracy: {accuracy[0]}, Iter2_Accuracy: {accuracy[1]}, Iter3_Accuracy: {accuracy[2]}, Iter4_Accuracy: {accuracy[3]}, Iter5_Accuracy: {accuracy[4]} \n Promedio_Accuracy: {accuracy_mean}")
        return accuracy_mean

    #Save model
    @staticmethod
    def model_storage(id_model: int, config: Configuration, X, y, method: ClassificationMethod):
        """[summary]

        Args:
            id_model (int): [description]
            config (Configuration): [description]
            X ([type]): [description]
            y ([type]): [description]
            method (ClassificationMethod): [description]
        """
        #Si el id_model existe -> actualizalo
        #Sino crealo 
        model = Classification.run_model_balanced(X, y, method)
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        dict_config_model = {
            'config': config,
            'model': model
        }
        #guardar modelos
        #save model train in the file
        dump(dict_config_model, f'models/{id_model}')
        #load the model
        # model1 = load('models/id_model')

    #Predict
    @staticmethod
    def predict_method(model, X, n_value: int):
        """[summary]

        Args:
            model ([type]): [description]
            X ([type]): [description]
            n_value (int): [description]
        """
        results = model.predict_proba(X)[0]
        prob_per_class_dictionary = dict(zip(model.classes_, results))
        results_ordered_by_probability = sorted(
                zip(model.classes_, results),
                key=lambda x: x[1],
                reverse=True
            )
        if n_value != None:
            n_results_ordered_by_probability = results_ordered_by_probability[0:n_value]
            print(f"A continuación las {n_value} clases con mejor probabilidad: {n_results_ordered_by_probability}")

        else:
            n_value = len(results_ordered_by_probability)
            n_results_ordered_by_probability = results_ordered_by_probability[0:n_value]
            print(f"A continuación las {n_value} clases con sus probabilidades: {n_results_ordered_by_probability}")

    #Model
    @staticmethod
    def run_model_balanced(X_train, y_train, method: ClassificationMethod):
        """[summary]

        Args:
            X_train ([type]): [description]
            y_train ([type]): [description]
            method (ClassificationMethod): [description]

        Returns:
            [type]: [description]
        """
        #clasificador a utilizar
        if method == ClassificationMethod.LOGISTIC_REGRESSION:
            clf = LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg",class_weight="balanced")
        if method == ClassificationMethod.SVM:
            clf = SVC(kernel='linear', probability=True, class_weight="balanced")
        if method == ClassificationMethod.BAYES:
            clf = MultinomialNB(class_weight="balanced")
        #Ajustamos los datos de entrenamiento en el clasificador usando fit(). Entrenar nuestro modelo
        clf.fit(X_train, y_train)
        return clf
