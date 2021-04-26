from tweetlib import * 
from collections import Counter
import numpy as np
import os
from demos.basic_spanish import run as basic_spanish_demo
from demos import demo_artistas

from tweetlib.config.config import Configuration
from tweetlib.definitions import Preprocessing, EncodingMethod, ClassificationMethod
from tweetlib.pipeline.execute_pipeline import TwitterPipeline

from tweetlib.data_set.data_set import DataSet
from tweetlib.data_set.deportistas import DataSetDeportistas
from tweetlib.data_set.politicos import DataSetPoliticos

# c = Configuration([
#         Preprocessing.STOP_WORDS,
#         Preprocessing.TOKENIZE
#     ],
#     EncodingMethod.MARKOV,
#     ClassificationMethod.SVM
# )

# ds = DataSetDeportistas()

# pipe = TwitterPipeline(c, ds)
# pipe.run()

# LIST-VECTORS
# #Por parametro entraria una lista de usuarios, los cuales serian las clases, y para cada clase, obtener la lista de tweets
# def list_vectors():
#     list_texts = SpanishTextSamples.get_all_texts()
#     vectors = []
#     for i in list_texts:
#         vectors.append(postagging(i, TaggingMethod.SPACY))
#     matriz = np.vstack(vectors)
#     print(matriz)
#     return matriz
  
if __name__ == '__main__':
    # nlp = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)
    # nlp = init_nlp(TaggingMethod.SPACY, Lang.EN, DictionarySize.MEDIUM)
    # list_vectors()

    # basic_spanish_demo()

#Tests
# for token in doc:
#     if token.pos_ == 'CCONJ':
#         print(token.text) 

# for token in doc:
#     if token.text == ':)':
#         print(token.pos_) 


# def stanza_postagging(text: str):
#     doc = nlp(text)

#     for sent in doc.sentences:
#         freq_dictionary = Counter([word.upos for word in sent.words])
#         print(freq_dictionary)
#         vector_stanza = [freq_dictionary['ADJ'], freq_dictionary['ADP'], freq_dictionary['ADV'], freq_dictionary['AUX'], freq_dictionary['CONJ'], freq_dictionary['CCONJ'], freq_dictionary['DET'], freq_dictionary['INTJ'], freq_dictionary['NOUN'], freq_dictionary['NUM'], freq_dictionary['PART'], freq_dictionary['PRON'], freq_dictionary['PROPN'], freq_dictionary['PUNCT'], freq_dictionary['SCONJ'], freq_dictionary['SYM'], freq_dictionary['VERB'], freq_dictionary['X'], freq_dictionary['SPACE']]
#         total_tokens_stanza = sum(freq_dictionary.values())
#         np_array_stanza = np.array(vector_stanza)
#         vector_frec = np_array_stanza/total_tokens_stanza
#         print(vector_frec)
# stanza.download('en')

        # print(f'word: {word.text} \tlemma: {word.lemma} \tpos: {word.upos}') 
        # freq_dictionary = Counter(word.upos)
        # print(freq_dictionary)

