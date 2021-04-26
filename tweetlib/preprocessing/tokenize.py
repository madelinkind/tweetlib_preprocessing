from tweetlib.definitions import TaggingMethod

def Tokenize(text: str, method: TaggingMethod):
    pass
    #implementar para spacy una lista de token
    #para stanza seria entrarle por parametro el processors
    # if method == TaggingMethod.SPACY:
    #     my_doc = nlp(text)

    #     # Create list of word tokens
    #     token_list = []
    #     for token in my_doc:
    #         token_list.append(token.text)
    #     print(token_list)
    # else
    #     processors = 'tokenize'