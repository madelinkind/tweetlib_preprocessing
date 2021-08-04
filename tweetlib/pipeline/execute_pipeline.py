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
# from tweetlib.singleton import NlpFactory

from tweetlib.preprocessing.prep_definitions import dict_preprocessing
from tweetlib.encoding.enc_definitions import dict_encoding
from tweetlib.singleton import Utils 

class TwitterPipeline(object):

    def __init__(self, config: Configuration, dataset: DataSet, classifier: Classification):
        super(TwitterPipeline, self).__init__()

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
        tagging_method_type = self.config.get_tagging_method()
        vectors = []
        #INITIALIZE THE LIBRARY TO USE
        nlp = Utils.load_nlp(tagging_method_type)
        #copy to data
        data_texts = data.copy()

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
        else:
            vector_encoding = encoding_method(data_texts, tagging_method_type.name, nlp)

        X = np.vstack(vector_encoding)

        # #classifier
        # y_test, pred_y = self.classifier.classification_method(X, y, classifier_type)
        # accuracy = self.classifier.classification_method(X, y, classifier_type)
        accuracy = self.classifier.classification_method(X, y, classifier_type)

