import os
import sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


from tweetlib.data_set.data_set import DataSet
from tweetlib.pipeline.execute_pipeline import TwitterPipeline
from tweetlib.config.configuration import Configuration
from tweetlib.definitions import Preprocessing, EncodingMethod, ClassificationMethod, TaggingMethod
from tweetlib.classification.classification import Classification

from tweetlib.data_set.artistas import DataSetArtistas

config = Configuration([
    Preprocessing.FIX_HASHTAG_TEXT,
    # Preprocessing.TOKENIZE, 
    Preprocessing.REMOVE_STOP_WORDS, 
    Preprocessing.LEMMATIZE
    ], 
    EncodingMethod.POSTAGGING, 
    ClassificationMethod.SVM,
    TaggingMethod.SPACY
)

data_set_artista = DataSetArtistas()

classifier = Classification()

pipeline = TwitterPipeline(config, data_set_artista, classifier)

if __name__ == "__main__":
    pipeline.run()


