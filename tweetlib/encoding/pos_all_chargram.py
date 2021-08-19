from tweetlib.encoding.all_chargrams import all_char_grams
from tweetlib.encoding.postagging import postagging_encoding
from tweetlib.definitions import TaggingMethod
from tweetlib.init_nlp import init_nlp

def pos_all_chargram(data_texts, tagging_method: TaggingMethod, nlp):
    all_chars = all_char_grams(data_texts)
    postagging = postagging_encoding(data_texts, tagging_method, nlp)
    return all_chars[0], all_chars[1], all_chars[2], postagging
