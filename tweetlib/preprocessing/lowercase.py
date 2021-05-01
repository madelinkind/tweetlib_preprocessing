
#Establecer todas las palabras a minúscula
def Lowercase(text: list):
    lowercase_text = []
    for word in text:
        lowercase_text.append(word.lower().strip())
    return lowercase_text