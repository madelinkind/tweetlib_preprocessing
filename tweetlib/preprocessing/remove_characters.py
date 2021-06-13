def RemoveCharacters (text: list, nlp):
    """Eliminar todo lo que no sea caracteres alfabéticos  en el corpus

    Args:
        text (list): Lista de tokens.
        nlp ([type]): Biblioteca de spacy, para utilizar sus atributos, en este caso "is_alpha".

    Returns:
        [type]: Lista sin caracteres alfanuméricos.
    """
    text_within_characters = []
    doc = nlp(" ".join(text))
    text_within_characters= [str(word) for word in doc if word.is_alpha]
    return text_within_characters