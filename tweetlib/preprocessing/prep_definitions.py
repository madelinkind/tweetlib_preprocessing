from tweetlib.preprocessing.clean_emoticons import CleanEmoticons
from tweetlib.preprocessing.lemmatize import Lemmatize
from tweetlib.preprocessing.remove_num import RemoveNum
from tweetlib.preprocessing.remove_punct import RemovePunct
from tweetlib.preprocessing.remove_stop_words import Stop_words
from tweetlib.preprocessing.remove_links import RemoveLinks
from tweetlib.preprocessing.tokenize import Tokenize
from tweetlib.preprocessing.lowercase import Lowercase
from tweetlib.preprocessing.remove_emails import RemoveEmails
from tweetlib.preprocessing.remove_characters import RemoveCharacters
from tweetlib.definitions import Preprocessing

dict_preprocessing = {
    Preprocessing.REMOVE_NUM: RemoveNum,
    Preprocessing.REMOVE_PUNCT: RemovePunct,
    Preprocessing.REMOVE_CHARACTERS: RemoveCharacters,
    Preprocessing.CLEAN_EMOTICONS: CleanEmoticons,
    Preprocessing.LEMMATIZE: Lemmatize,
    Preprocessing.STOP_WORDS: Stop_words,
    Preprocessing.REMOVE_LINKS: RemoveLinks,
    Preprocessing.REMOVE_EMAILS: RemoveEmails,
    Preprocessing.TOKENIZE: Tokenize,
    Preprocessing.LOWERCASE: Lowercase
}