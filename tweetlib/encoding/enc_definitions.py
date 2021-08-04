from tweetlib.encoding.postagging import postagging_encoding
from tweetlib.encoding.char2grams import char_2_gram
from tweetlib.encoding.char3grams import char_3_gram
from tweetlib.encoding.char4grams import char_4_gram
from tweetlib.encoding.markov import Markov
from tweetlib.definitions import EncodingMethod

dict_encoding = {
    EncodingMethod.BIGRAM: char_2_gram,
    EncodingMethod.TRIGRAM: char_3_gram,
    EncodingMethod.CUATRIGRAM: char_4_gram,
    EncodingMethod.POSTAGGING: postagging_encoding,
    EncodingMethod.MARKOV: Markov
}