from enum import Enum

import stanza
import spacy, en_core_web_md, es_core_news_md, es_core_news_sm, es_core_news_lg
from spacy import displacy

from .definitions import *

#INITIALIZE THE LIBRARY TO USE
def init_nlp(tagging_method: int, lang: int, size: int = DictionarySize.SMALL):
    if tagging_method == TaggingMethod.STANZA:
        if lang == Lang.ES:
            nlp = stanza.Pipeline(lang='es', processors='tokenize,lowercase,lemma,pos')
            return nlp
        elif lang == Lang.EN:
            nlp = stanza.Pipeline(lang='en', processors='tokenize,lowercase,lemma,pos')
            return nlp
        else:
            raise Exception('')
    
    elif TaggingMethod.SPACY:
        if size == DictionarySize.SMALL and lang == Lang.ES:
            nlp = es_core_news_sm.load()
            return nlp
        elif size == DictionarySize.MEDIUM and lang == Lang.ES:
            nlp = es_core_news_md.load()
            return nlp
        elif size == DictionarySize.LARGE and lang == Lang.ES:
            nlp = es_core_news_lg.load()
            return nlp
        elif size == DictionarySize.SMALL and lang == Lang.EN:
            nlp = en_core_web_sm.load()
            return nlp
        elif size == DictionarySize.MEDIUM and lang == Lang.EN:
            nlp = en_core_web_md.load()
            return nlp
        elif size == DictionarySize.LARGE and lang == Lang.EN:
            nlp = en_core_web_lg.load()
            return nlp
        else:
            raise ValueError("Could not build nlp with the given parameters")