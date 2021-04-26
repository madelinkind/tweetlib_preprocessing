from tweetlib.preprocessing.clean_emoticons import CleanEmoticons
from tweetlib.preprocessing.lemmatize_lowercase import Lemmatize
from tweetlib.preprocessing.clean_tweet import CleanTweets
from tweetlib.preprocessing.remove_stop_words import Stop_words
from tweetlib.preprocessing.tokenize import Tokenize
from tweetlib.definitions import Preprocessing


dict_preprocessing = {
    Preprocessing.CLEAN_TWEET: CleanTweets,
    Preprocessing.CLEAN_EMOTICONS: CleanEmoticons,
    Preprocessing.LEMMATIZE: Lemmatize,
    Preprocessing.STOP_WORDS: Stop_words,
    Preprocessing.TOKENIZE: Tokenize
}