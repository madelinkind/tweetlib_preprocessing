# Spacy
def RemoveNum (text: list, nlp):
    """Elimina los números de un corpus

    Args:
        text (list[str]): Lista de tokens
        nlp (spacy.lang.es.Spanish): Biblioteca de spacy, para utilizar sus atributos, en este caso "like_num"

    Returns:
        list[str]: Lista sin números.
    """
    text_within_num = []
    doc = nlp(" ".join(text))
    text_within_num = [str(word) for word in doc if not word.like_num]
    return text_within_num