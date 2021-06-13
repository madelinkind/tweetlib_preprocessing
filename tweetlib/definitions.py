from enum import Enum

# TYPES OF LIBRARIES
class TaggingMethod(Enum):
    STANZA = 1
    SPACY = 2

# VOCABULARY SIZE
class DictionarySize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

# TYPE OF LANGUAGE
class Lang(Enum):
    ES = 1
    EN = 2

# TYPE OF USER
class TypeUser():
    politico = 'politico'
    artista = 'artista'
    deportista = 'deportista'
    youtuber = 'youtuber'
    all_results = 'todos'

# TYPE OF DATASET
# class DATASET(Enum):
#     politico = 1
#     artista = 2
#     deportista = 3
#     youtuber = 4
#     all_results = 5

# TYPE PREPROCESSING
class Preprocessing(Enum):
    REMOVE_NUM = 1
    CLEAN_EMOTICONS = 2
    LEMMATIZE = 3
    STOP_WORDS = 4
    REMOVE_LINKS = 5
    TOKENIZE = 6
    LOWERCASE = 7
    REMOVE_EMAILS = 8
    REMOVE_PUNCT = 9
    REMOVE_CHARACTERS = 10

# TYPE ENCODING
class EncodingMethod(Enum):
    TRIGRAM = 1
    CUATRIGRAM = 2
    POSTAGGING = 3
    MARKOV = 4

# TYPE CLASSIFICATION
class ClassificationMethod(Enum):
    SVM = 1
    SVM_RBC = 2
    PMSVM = 3
    BAYES = 4
    LOGISTIC_REGRESSION = 5
