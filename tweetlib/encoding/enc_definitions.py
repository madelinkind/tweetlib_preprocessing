from tweetlib.encoding.postagging import postagging_encoding
from tweetlib.encoding.word_ngrams import Bigram
from tweetlib.encoding.markov import Markov
from tweetlib.definitions import EncodingMethod

dict_encoding = {
    EncodingMethod.NGRAM_WORD: Bigram,
    EncodingMethod.POSTAGGING: postagging_encoding,
    EncodingMethod.MARKOV: Markov
}