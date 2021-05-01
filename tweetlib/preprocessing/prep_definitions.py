from tweetlib.preprocessing.clean_emoticons import CleanEmoticons
from tweetlib.preprocessing.lemmatize import Lemmatize
from tweetlib.preprocessing.clean_tweet import CleanTweets
from tweetlib.preprocessing.remove_stop_words import Stop_words
from tweetlib.preprocessing.remove_links import RemoveLinks
from tweetlib.preprocessing.tokenize import Tokenize
from tweetlib.preprocessing.lowercase import Lowercase
from tweetlib.definitions import Preprocessing

dict_preprocessing = {
    Preprocessing.CLEAN_TWEET: CleanTweets,
    Preprocessing.CLEAN_EMOTICONS: CleanEmoticons,
    Preprocessing.LEMMATIZE: Lemmatize,
    Preprocessing.STOP_WORDS: Stop_words,
    Preprocessing.REMOVE_LINKS: RemoveLinks,
    Preprocessing.TOKENIZE: Tokenize,
    Preprocessing.LOWERCASE: Lowercase
}