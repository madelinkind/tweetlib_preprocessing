from spacymoji import Emoji
# import es_core_news_lg

def CleanEmoticons(text: list, nlp):
    """Elimina los emoji de un corpus

    Args:
        text (list[str]): Lista de tokens.
        nlp ([type]): Biblioteca de spacy, para utilizar sus atributos, en este caso "emoji".

    Returns:
        list[str]: Lista sin emoji.
    """
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
        return list_within_emoji
    else:
        return text

# if __name__ == '__main__':
#     CleanEmoticons(text)

    # if doc._.has_emoji == True:
    #         for i in doc:
    #             if i._.is_emoji == False:
    #                 list_within_emoji.append(i)
    #         return list_within_emoji
    #     else:
    #         return text