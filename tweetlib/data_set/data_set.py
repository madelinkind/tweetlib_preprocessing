
import os
import sys

# Django specific settings

FILE = __file__
DATA_SET_FOLDER = os.path.split(FILE)[0]
TWEET_LIB_FOLDER = os.path.split(DATA_SET_FOLDER)[0]
PROJECT_FOLDER = os.path.split(TWEET_LIB_FOLDER)[0]

sys.path.append(PROJECT_FOLDER)
sys.path.append(f"{PROJECT_FOLDER}/orm")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import Tweet, TwitterUser
from tweetlib.definitions import TypeUser

class DataSet():

    def __init__(self, user_type: TypeUser):
        data, y = self.get_tuple_tweets_user(user_type)
        self.data = data
        self.y = y

#Se obtiene la tupla (list de tweets (data) y list de user (y)) por tipo de usuario.
    def get_tuple_tweets_user(self, user_type: TypeUser):
        if user_type == TypeUser.politico:
            return self.get_user_tweets(user_type)
        if user_type == TypeUser.youtuber:
            return self.get_user_tweets(user_type)
        if user_type == TypeUser.artista:
            return self.get_user_tweets(user_type)
        if user_type == TypeUser.deportista:
            return self.get_user_tweets(user_type)
        elif user_type == TypeUser.all_results:
            return self.get_user_tweets(user_type) 
        else:
            raise Exception("You must enter a valid user type, See TypeUser.")

#Devuelve lista de usuario segun el tipo
    def get_list_users(self, user_type: TypeUser) -> list:
        if user_type == TypeUser.all_results:
            users_map = map(
                lambda item: item['screen_name'], 
                TwitterUser.objects.values('screen_name')
            )
            list_users = list(users_map)
            get_user_tweets(list_users)
        else:
            users_map = map(lambda item: item['screen_name'], TwitterUser.objects.filter(type_user=user_type).values('screen_name'))
            list_users = list(users_map)
        return list_users

# Se obtiene una tupla (lista de tweets, lista del mismo usuario repetido con misma longitud que la lista de tweets)
    def get_user_tweets(self, user_type: TypeUser):

        list_users = self.get_list_users(user_type)
            # Lists of Data(texts) and Class(y) in (es)
        data = []
        y = []
        for user in list_users:
            # cont = 0
            user_name = TwitterUser.objects.get(screen_name=user)
            last_tweets = Tweet.objects.filter(twitter_user=user_name.id).all()[:3]
            for tweet in last_tweets:
                if not tweet.is_retweet and tweet.tweet_lang == 'es':
                    data.append(tweet.tweet_text)
                    y.append(user_name.id)
                #     cont = cont + 1
                # if cont == 1000:
                #     break
        return data, y

    def get_data(self):
        return self.data

    def get_y(self):
        return self.y

    def is_valid():
        if self.data is None or not len(self.data) or self.y is None or not len(self.y):
            return False 

        return len(self.data) == len(self.y)
