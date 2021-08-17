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
from tweetlib.definitions import ClassificationMethod
from tweetlib.classification.classification import Classification
# from tweetlib.preprocessing.remove_stop_words import Stop_words
from tweetlib.definitions import TaggingMethod, DictionarySize, Lang, TypeTask
from tweetlib.init_nlp import init_nlp
# from tweetlib.singleton import NlpFactory

from tweetlib.preprocessing.prep_definitions import dict_preprocessing
from tweetlib.encoding.enc_definitions import dict_encoding
from tweetlib.classification.task_definition import dict_task 
from tweetlib.singleton import Utils 

class TwitterPipeline(object):

    def __init__(self, config: Configuration, dataset: DataSet, classifier: Classification, task: TypeTask, text: str = None, id_model: int = None, n_value: int = None):
        super(TwitterPipeline, self).__init__()

        self.config = config
        self.dataset = dataset
        self.classifier = classifier
        self.task = task
        self.text = text
        self.id_model = id_model
        self.n_value = n_value

    def run(self):
        # get data and classes from self.data
        data = self.dataset.get_data()
        y = self.dataset.get_y()
        preprocessing_list = self.config.get_preprocessing_methods()
        encoding = self.config.get_encoding_method()
        classifier_type = self.config.get_classification_method()
        tagging_method_type = self.config.get_tagging_method()
        # type_user = self.config.get_type_user()
        # vectors = []
        #INITIALIZE THE LIBRARY TO USE
        nlp = Utils.load_nlp(tagging_method_type)
        #copy to data
        data_texts = data.copy()

        type_task = dict_task[self.task]
        if self.task.name == 'VALIDATE_MODEL' or self.task.name == 'MODEL_STORAGE':
            for preprocessing in preprocessing_list:
                prep_method = dict_preprocessing[preprocessing]
                if preprocessing.name != 'LOWERCASE' and preprocessing.name != 'REMOVE_STOP_WORDS' and preprocessing.name != 'MENTIONS':
                    for idx, text in enumerate(data_texts):
                        prep = prep_method(text)
                        data_texts[idx] = prep
                else:
                    for idx, text in enumerate(data_texts):
                        prep = prep_method(text)
                        data_texts[idx] = prep

            # apply encoding
            encoding_method = dict_encoding[encoding]

            if encoding.name == 'BIGRAM' or encoding.name == 'TRIGRAM' or encoding.name == 'CUATRIGRAM':
                vector_encoding = encoding_method(data_texts)
            elif encoding.name == 'ALL_CHARGRAM':
                vectors = encoding_method(data_texts)
                vector_encoding = np.concatenate(vectors[0], vectors[1], vectors[2])
            elif encoding.name == 'POS_ALL_CHARGRAM':
                vectors = encoding_method(data_texts, tagging_method_type.name, nlp)
                vector_encoding = np.concatenate(vectors[0], vectors[1], vectors[2], vectors[3])
            #postagging
            else:
                vector_encoding = encoding_method(data_texts, tagging_method_type.name, nlp)

            X = np.vstack(vector_encoding)

            # #classifier (validate_model)
            # y_test, pred_y = self.classifier.classification_method(X, y, classifier_type)
            # accuracy = self.classifier.classification_method(X, y, classifier_type)

            # instancia de Classification
            # c = self.classifier



            if self.task.name == 'VALIDATE_MODEL':
                validate_model = type_task(self, X, y, classifier_type)
            else:
                # save_model = self.classifier.save_model(X, y, preprocessing_list, encoding, classifier_type, tagging_method_type, type_task, type_user)
                model_storage = type_task(self.id_model, self.config, X, y, classifier_type)


        # accuracy = self.classifier.classification_method(X, y, classifier_type). n_value cantidad de clases con mejor presicion
        elif self.task.name == 'PREDICTION':
            predict_method = type_task(self.id_model, self.text, self.n_value)

