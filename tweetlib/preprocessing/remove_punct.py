# Spacy
def RemovePunct (text: list, nlp):
    """Elimina los signos de puntuación de un corpus

    Args:
        text (list[str]): Lista de tokens
        nlp (spacy.lang.es.Spanish): Biblioteca de spacy, para utilizar sus atributos, en este caso "is_punct"

    Returns:
        list[str]: Lista sin signos de puntuación.
    """
    text_within_punct = []
    doc = nlp(" ".join(text))
    text_within_punct = [str(word) for word in doc if not word.is_punct]
    return text_within_punct