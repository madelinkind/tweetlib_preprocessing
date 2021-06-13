#Crear un diccionario con todas las combinaciones de 3gram, donde la llave es el trigram
#y el valor es la frecuencia de repetición.
#X= Convertir luego el diccionario a un vector que contenga los valores de ese diccionario.
#y= Crear 

import os
import sys

FILE = __file__
DATA_SET_FOLDER = os.path.split(FILE)[0]
TWEET_LIB_FOLDER = os.path.split(DATA_SET_FOLDER)[0]
PROJECT_FOLDER = os.path.split(TWEET_LIB_FOLDER)[0]

sys.path.append(PROJECT_FOLDER)

from tweetlib.encoding.char_grams import CharGrams
text = ['studenú', 'qwed', 'prueba', 'trigramram', 'i\'']


# CharGrams(text,n=3)

if __name__ == '__main__':
    CharGrams(text,n=3)