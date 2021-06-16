from spacymoji import Emoji
import es_core_news_lg
# from spacy.tokens import retokenize


# text = ['🤾', '🏻\u200d', '♀', '️', 'La', 'selección', 'española', 'vence', 'a', 'Noruega', 'y', 'se', 'coloca', 'a', 'un', 'paso','de','ganar','el','Mundial','femenino','de','balonmano','👏','🏻','\n','¡','Muc','…','https://t.co/IbVGXUz8Lb']
# text = [ '\n', '🤾','♀', '👏', '🏻\u200d', '️', 'La', 'selección', 'española', 'vence', 'a', 'Noruega', 'y', '', '🏻','\n','¡','Muc','…', 'https://t.co/IbVGXUz8Lb']
text = ['🤾', '🏻\u200d', '♀', '️', 'La', 'selección', 'española']
def CleanEmoticons(text: list):
    """Elimina los emoji de un corpus

    Args:
        text (list[str]): Lista de tokens.
        nlp ([type]): Biblioteca de spacy, para utilizar sus atributos, en este caso "emoji".

    Returns:
        list[str]: Lista sin emoji.
    """
    nlp = es_core_news_lg.load()
    list_within_emoji = []
    emoji = Emoji(nlp)
    if not nlp.has_pipe("emoji"):
        nlp.add_pipe(emoji, first=True)
    doc = nlp(" ".join(text))
    if doc._.has_emoji:
        list_within_emoji = [str(word) for word in doc if not word._.is_emoji]
        # for i in doc:
        #     if not i._.is_emoji:
        #         list_within_emoji.append(i)
        print(list_within_emoji)
        # return list_within_emoji
    else:
        print(text)
        # return text

if __name__ == '__main__':
    CleanEmoticons(text)

# if __name__ == '__main__':
#     CleanEmoticons(text)

    # if doc._.has_emoji == True:
    #         for i in doc:
    #             if i._.is_emoji == False:
    #                 list_within_emoji.append(i)
    #         return list_within_emoji
    #     else:
    #         return text