from tweetlib.encoding.postagging import postagging_encoding
from tweetlib.encoding.char3grams import CharGrams
from tweetlib.encoding.char4grams import CharGrams
from tweetlib.encoding.markov import Markov
from tweetlib.definitions import EncodingMethod

dict_encoding = {
    EncodingMethod.TRIGRAM: CharGrams,
    EncodingMethod.CUATRIGRAM: CharGrams,
    EncodingMethod.POSTAGGING: postagging_encoding,
    EncodingMethod.MARKOV: Markov
}