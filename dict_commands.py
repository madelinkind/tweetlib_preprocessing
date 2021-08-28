from tweetlib.definitions import EncodingMethod, ClassificationMethod, Preprocessing, TaggingMethod

# dict_commands = {
#     'create-model': TypeTask.MODEL_STORAGE,
#     'update-model': TypeTask.MODEL_STORAGE,
#     'find-author': TypeTask.PREDICTION,
#     'validate-new-model': TypeTask.VALIDATE_MODEL,
#     'validate-existing-model': TypeTask.VALIDATE_MODEL
# }

dict_classifier = {
    'SVM': ClassificationMethod.SVM,
    'LR': ClassificationMethod.LOGISTIC_REGRESSION,
    'BAYES': ClassificationMethod.BAYES
}

dict_encoding = {
    'POS': EncodingMethod.POSTAGGING,
    'BIGRAM': EncodingMethod.BIGRAM,
    'TRIGRAM': EncodingMethod.TRIGRAM,
    'CUATRIGRAM': EncodingMethod.CUATRIGRAM,
    'POSALLGRAM': EncodingMethod.POS_ALL_CHARGRAM,
    'ALLGRAM': EncodingMethod.ALL_CHARGRAM
}

dict_prep = {
    'TOKENIZE': Preprocessing.FIX_HASHTAG_TEXT,
    'ALPHA_NUMERIC': Preprocessing.REMOVE_ALPHA_NUMERIC,
    'NUM': Preprocessing.NUM,
    'PUNCT': Preprocessing.PUNCT,
    'EMAILS': Preprocessing.EMAILS,
    'LINKS': Preprocessing.LINKS,
    'LOWERCASE': Preprocessing.LOWERCASE,
    'LEMMATIZE': Preprocessing.LEMMATIZE,
    'EMOTICONS': Preprocessing.EMOTICONS,
    'STOP_WORDS': Preprocessing.REMOVE_STOP_WORDS,
    'MENTIONS': Preprocessing.MENTIONS,
    'HASHTAG': Preprocessing.HASHTAG
}

dict_tagging = {
    'SPACY': TaggingMethod.SPACY,
    'STANZA': TaggingMethod.STANZA
}