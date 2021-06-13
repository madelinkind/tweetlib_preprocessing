import itertools

class NGramUtils(object):
    ngram_dict = {}
    dict_ngram = {}

    @staticmethod
    def ngrams(n):
        if n in NGramUtils.ngram_dict:
            return NGramUtils.ngram_dict[n]
        else:
            # compute ngrams
            list_alpha_numeric = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTÁÉÍÓÚáéíóú1234567890@#`~ªº!"·$%&/()=?¿¡;,.:_-\'"]\[}{|<>'
            result_dict = ["".join(p) for p in itertools.product(list_alpha_numeric, repeat=n)]

            for i in result_dict:
                NGramUtils.dict_ngram[i] = 0

            # store ngrams in 'NGramUtils.ngram_dict'
            NGramUtils.ngram_dict[n] = NGramUtils.dict_ngram
            # return result
            return NGramUtils.ngram_dict[n]