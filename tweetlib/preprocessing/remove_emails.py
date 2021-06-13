# Spacy
def RemoveEmails (text: list, nlp):
    """Elimina las direcciones de correos de un corpus

    Args:
        text (list[str]): Lista de tokens
        nlp (spacy.lang.es.Spanish): Biblioteca de spacy, para utilizar sus atributos, en este caso "like_email"

    Returns:
        list[str]: Lista sin direcciones de correos.
    """

    text_within_emails = []

    # nlp = es_core_news_lg.load()
    doc = nlp(" ".join(text))
    # for word in doc:
    #     if word.like_email == False:
    #         text_within_emails.append(word)
    text_within_emails = [str(word) for word in doc if not word.like_email]

    return text_within_emails