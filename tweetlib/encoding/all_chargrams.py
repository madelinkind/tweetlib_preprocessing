from tweetlib.encoding.char2grams import char_2_gram
from tweetlib.encoding.char3grams import char_3_gram
from tweetlib.encoding.char4grams import char_4_gram


def all_char_grams(data_texts):
    bi = char_2_gram(data_texts)
    tri = char_3_gram(data_texts)
    cuatri = char_4_gram(data_texts)
    return bi, tri, cuatri