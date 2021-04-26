from spacymoji import Emoji
from tweetlib.init_nlp import init_nlp
from tweetlib.definitions import TaggingMethod, DictionarySize, Lang

def CleanEmoticons(text: str):
    nlp = init_nlp(TaggingMethod.SPACY, Lang.ES, size=DictionarySize.MEDIUM)
    list_within_emoji = []
    emoji = Emoji(nlp)
    nlp.add_pipe(emoji, first=True)

    doc = nlp(text)
    if doc._.has_emoji == True:
        for i in doc:
            if i._.is_emoji == False:
                list_within_emoji.append(i)
        return list_within_emoji
    else:
        return text
