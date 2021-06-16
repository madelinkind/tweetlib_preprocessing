import os
import sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from tweetlib.data_set.data_set import DataSet
from tweetlib.pipeline.execute_pipeline import TwitterPipeline
from tweetlib.config.configuration import Configuration
from tweetlib.definitions import Preprocessing, EncodingMethod, ClassificationMethod
from tweetlib.classification.classification import Classification

from tweetlib.data_set.politicos import DataSetPoliticos

config = Configuration([
        Preprocessing.TOKENIZE,
        # Preprocessing.REMOVE_CHARACTERS,
        # Preprocessing.REMOVE_NUM,
        # Preprocessing.REMOVE_PUNCT,
        # Preprocessing.REMOVE_EMAILS,
        # Preprocessing.REMOVE_LINKS,
        # Preprocessing.LOWERCASE,
        # Preprocessing.LEMMATIZE,
        Preprocessing.CLEAN_EMOTICONS, 
        # Preprocessing.STOP_WORDS
    ], 
    # EncodingMethod.POSTAGGING,
    EncodingMethod.TRIGRAM, 
    # ClassificationMethod.LOGISTIC_REGRESSION
    ClassificationMethod.SVM
)

data_set_politicos = DataSetPoliticos()

classifier = Classification()

pipeline = TwitterPipeline(config, data_set_politicos, classifier)

if __name__ == "__main__":
    pipeline.run()


