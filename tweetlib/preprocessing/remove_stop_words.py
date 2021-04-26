from spacy.lang.es.stop_words import STOP_WORDS

# para observar las palabras dentro de la lista lo único que se #   # tiene que hacer eso imprimir
#print(list(STOP_WORDS)[:30])

text = ['además', 'ir', ':(', ':)', '']

def Stop_words(text):
    list_text = []
    #Para filtrar stopwords
    for word in text:
        if not word in STOP_WORDS:
            list_text.append(word)
    print(list_text)
    # return list_text

if __name__ == '__main__':
    Stop_words(text)