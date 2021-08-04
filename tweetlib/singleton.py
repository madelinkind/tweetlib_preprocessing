import itertools
from tweetlib.definitions import TaggingMethod, DictionarySize, Lang
from tweetlib.init_nlp import init_nlp

class Utils(object):
    ngram_dict = {}
    dict_ngram = {}
    dict_nlp = {}


    @staticmethod
    def ngrams(n):
        if n in Utils.ngram_dict:
            return Utils.ngram_dict[n]
        else:
            # compute ngrams
            list_alpha_numeric = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚáéíóú1234567890@#/()=?¿¡;,.:…_-\'"]\[}{|<>'
            result_dict = ["".join(p) for p in itertools.product(list_alpha_numeric, repeat=n)]

            for i in result_dict:
                Utils.dict_ngram[i] = 0

            # store ngrams in 'NGramUtils.ngram_dict'
            Utils.ngram_dict[n] = Utils.dict_ngram
            # return result
            return Utils.ngram_dict[n]

    def load_nlp(nlp):
        if nlp.value in Utils.dict_nlp:
            return Utils.dict_nlp[nlp.value]

        if nlp.name == 'SPACY':
            Utils.dict_nlp[nlp.value] = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)
        elif nlp.name == 'STANZA':
            Utils.dict_nlp[nlp.value] = init_nlp(TaggingMethod.STANZA, Lang.ES, size=DictionarySize.MEDIUM)

        return Utils.dict_nlp[nlp.value]
