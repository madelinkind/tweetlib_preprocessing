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
# from tweetlib.definitions import TaggingMethod
from tweetlib.classification.classification import Classification
# from tweetlib.preprocessing.remove_stop_words import Stop_words
from tweetlib.definitions import TaggingMethod, DictionarySize, Lang
from tweetlib.init_nlp import init_nlp

from tweetlib.preprocessing.prep_definitions import dict_preprocessing
from tweetlib.encoding.enc_definitions import dict_encoding

#INITIALIZE THE LIBRARY TO USE
# nlp = init_nlp(TaggingMethod.STANZA, Lang.ES, size=DictionarySize.MEDIUM)
nlp = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)

class TwitterPipeline(object):

    def __init__(self, config: Configuration, dataset: DataSet, classifier: Classification):
        super(TwitterPipeline, self).__init__()

#modificado por mi
        # data = self.run()
        # self.data = data

        self.config = config
        self.dataset = dataset
        self.classifier = classifier

    def run(self):
        # get data and classes from self.data
        data = self.dataset.get_data()
        y = self.dataset.get_y()
        preprocessing_list = self.config.get_preprocessing_methods()
        encoding = self.config.get_encoding_method()
        classifier_type = self.config.get_classificaion_method()
        vectors = []
        #INITIALIZE THE LIBRARY TO USE
        # nlp = init_nlp(TaggingMethod.STANZA, Lang.ES, size=DictionarySize.MEDIUM)
        nlp = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)
        #copy to data
        data_texts = data.copy()
        # for each preprocessing in self.config
            # apply preprocessing to data
        for preprocessing in preprocessing_list:
            prep_method = dict_preprocessing[preprocessing]
            if preprocessing.name != 'LOWERCASE' and preprocessing.name != 'STOP_WORDS':
                for idx, text in enumerate(data_texts):
                    prep = prep_method(text, nlp)
                    data_texts[idx] = prep
            else:
                for idx, text in enumerate(data_texts):
                    prep = prep_method(text)
                    data_texts[idx] = prep

        # apply encoding
        encoding_method = dict_encoding[encoding]
        for text in data_texts:
            if encoding.name == 'TRIGRAM' or encoding.name == 'CUATRIGRAM':
                encoding_result = encoding_method(text, 2)
            else:
                encoding_result = encoding_method(str(text), TaggingMethod.SPACY)
            vectors.append(encoding_result)
        X = np.vstack(vectors)

        # #classifier
        # y_test, pred_y = self.classifier.classification_method(X, y, classifier_type)
        accuracy = self.classifier.classification_method(X, y, classifier_type)

        # #mostrar los resultados
        # conf_matrix = confusion_matrix(y_test, pred_y)
        # plt.figure(figsize=(12, 12))
        # LABELS= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
        # plt.title("Confusion matrix")
        # plt.ylabel('True class')
        # plt.xlabel('Predicted class')
        # plt.show()
        # print (classification_report(y_test, pred_y))

# #modificado por mi
#      #definimos funcion para mostrar los resultados
#     def show_results(self, y_test, pred_y):

#         conf_matrix = confusion_matrix(y_test, pred_y)
#         plt.figure(figsize=(12, 12))
#         LABELS= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
#         plt.title("Confusion matrix")
#         plt.ylabel('True class')
#         plt.xlabel('Predicted class')
#         plt.show()
#         print (classification_report(y_test, pred_y))
        
        # # classify
        # #Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
        # #dividimos en sets de entrenamiento y test
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # def run_model_balanced(X_train, X_test, y_train, y_test):
        #     clf = LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg",class_weight="balanced")
        #     clf.fit(X_train, y_train)
        #     return clf
    
        # #ejecutamos el modelo "tal cual"
        # model = run_model_balanced(X_train, X_test, y_train, y_test)

        # pred_y = model.predict(X_test)

        # #definimos funciona para mostrar los resultados
        # def mostrar_resultados(y_test, pred_y):
        #     conf_matrix = confusion_matrix(y_test, pred_y)
        #     plt.figure(figsize=(12, 12))
        #     LABELS= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #     sns.heatmap(conf_matrix, xticklabels=LABELS, yticklabels=LABELS, annot=True, fmt="d");
        #     plt.title("Confusion matrix")
        #     plt.ylabel('True class')
        #     plt.xlabel('Predicted class')
        #     plt.show()
        #     print (classification_report(y_test, pred_y))
        
        # mostrar_resultados(y_test, pred_y)
