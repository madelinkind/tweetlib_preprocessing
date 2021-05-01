from tweetlib.definitions import TaggingMethod, DictionarySize, Lang
from tweetlib.init_nlp import init_nlp

#Tokenizar el texto
def Tokenize(text: str):
    # Create list of word tokens
    token_list = []
    nlp = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)
    my_doc = nlp(text)
    for token in my_doc:
        token_list.append(token.text)
    return token_list