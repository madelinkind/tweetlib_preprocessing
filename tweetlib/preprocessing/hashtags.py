import spacy
# import es_core_news_md


from spacy.matcher import Matcher
from spacy.tokens import Token

from tweetlib.singleton import Utils
from tweetlib.definitions import TaggingMethod

nlp = Utils.load_nlp(TaggingMethod.SPACY)

#Vector que devuelve una lista sin hashtag, otra con el texto incluyendo los hashtag correctamente  y el total de hashtag del texto. 
#Cambio de nomre de rm_hashtags a tool_hashtags

def tool_hashtags(text: list):
    # nlp = es_core_news_md.load()
    matcher = Matcher(nlp.vocab)
    matcher.add("HASHTAG", [[{"ORTH": "#"}, {"IS_ASCII": True}]])
    #Aqui me daba error, porque "is_hashtag" ya estaa agregado a Token, utilizo Token.has_extension 
    # para validar si ya se encuentra, de lo contrario se agrega. ver Documentación https://spacy.io/api/token 
    if not Token.has_extension("is_hashtag"):
        Token.set_extension("is_hashtag", default=False)
    within_hash = []
    with_hash = [] 
    # doc = nlp(" ".join(text))
    doc = nlp(text)
    matches = matcher(doc)
    hashtags = []
    for match_id, start, end in matches:
        if doc.vocab.strings[match_id] == "HASHTAG":
            hashtags.append(doc[start:end])
    with doc.retokenize() as retokenizer:
        for span in hashtags:
            # print(hashtags)
            retokenizer.merge(span)
            for token in span:
                if not token._.is_hashtag:
                  token._.is_hashtag = True 
                #   print(token)
    for token in doc:
        # print(token.text, token._.is_hashtag)
        if not token._.is_hashtag:
            within_hash.append(token.text)
            with_hash.append(token.text)
        else:
            with_hash.append(token.text)
    # print(within_hash, with_hash, len(hashtags))
    vector = within_hash, with_hash, len(hashtags)
    # print(vector[1])

    return vector

def rm_hashtags(text):
    if type(text) == str:
        text_string = text
    else:
        text_string = " ".join(text)
    within_hashtag = tool_hashtags(text_string)
    return within_hashtag[0]

#Texto con hashtag, solucion al error que la libreria de spacy tiene a la hora de tokenizar, ya que divide el
# el caracter # de la palabra. Este proceso lo que hace es devolver el texto con los hashtag correctamente representados
def fix_hashtags_in_text(text):
    with_hashtag = tool_hashtags(text)
    # print(with_hashtag[1])
    return with_hashtag[1]

def count_hashtags(text):
    if type(text) == str:
        text_string = text
    else:
        text_string = " ".join(text)
    count_hashtag_text = tool_hashtags(text_string)
    return count_hashtag_text[2] 


if __name__ == '__main__':
    rm_hashtags(text)