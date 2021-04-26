import os
import sys

FILE = __file__
DATA_SET_FOLDER = os.path.split(FILE)[0]
TWEET_LIB_FOLDER = os.path.split(DATA_SET_FOLDER)[0]
PROJECT_FOLDER = os.path.split(TWEET_LIB_FOLDER)[0]

sys.path.append(PROJECT_FOLDER)

from tweetlib.definitions import TaggingMethod, DictionarySize, Lang
from tweetlib.init_nlp import init_nlp
# from tweetlib.definitions import TaggingMethod

# text = """Pepe es un gobernate capaz, es derechista, y aboga por un patido pluripartidista :)"""
def Lemmatize(text: str):
    lem_text = []
    nlp = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)
    lem_doc = nlp(text)
    for lem_word in lem_doc:
        lem_text.append(lem_word.lemma_.lower().strip())
    #strip para quitar espacios en blanco
    print (lem_text)
    # else
    #     processors = 'lemma', 'lowercase'

# if __name__ == '__main__':
#     Lemmatize(text)