from tweetlib.definitions import TaggingMethod
from tweetlib.init_nlp import init_nlp

def Lemmatize(text: str, method: TaggingMethod):
    pass
    # lem_text = []
    # if method == TaggingMethod.SPACY:
    #     lem_doc = nlp(text)
    #     for lem_word in lem_doc:
    #         lem_text.append(lem_word.lemma_.lower())
    #     #strip para quitar espacios en blanco
    #     return lem_text.strip()
    # else
    #     processors = 'lemma', 'lowercase'