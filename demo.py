import os
import sys

from crawler.io import load_users_list_from_file
import crawler.config as conf
from crawler.engine import TwitterEngine
from crawler.storage import DBStorage
from datetime import datetime, date, time, timedelta

# ----------------------------------------------------------

# Django specific settings
sys.path.append('./orm')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import Tweet, TwitterUser

#save model
from joblib import dump, load
from tweetlib.classification.classification import Classification
from tweetlib.config.configuration import Configuration
from tweetlib.definitions import TypeDataSet, TypeTask, Preprocessing, EncodingMethod, ClassificationMethod
from dict_commands import dict_commands
from tweetlib.pipeline.execute_pipeline import TwitterPipeline
# ----------------------------------------------------------

# # load users list

def download_all_tweets_users():
    users_map = map(lambda item: item['screen_name'], TwitterUser.objects.order_by('id').values('screen_name'))
    users_list = list(users_map)
    
    dbs = DBStorage()
    te = TwitterEngine(
        access_token = conf.ACCESS_TOKEN,
        access_token_secret = conf.ACCESS_TOKEN_SECRET,
        consumer_key = conf.CONSUMER_KEY,
        consumer_key_secret = conf.CONSUMER_KEY_SECRET,
        usernames = users_list,
    
        storage = dbs
    )
    
    te.download_tweets()
# user = 'Ninelconde'
def download_all_tweets_user(user, typeuser=None):
#Si esta en DB lo descargamos directamente, de lo contrario insertamos en DB y descargamos los tweets.
    if not TwitterUser.objects.filter(screen_name=user).exists():
        TwitterUser.objects.create(screen_name=user)

    users_list = [user]

    dbs = DBStorage()
    te = TwitterEngine(
        access_token = conf.ACCESS_TOKEN,
        access_token_secret = conf.ACCESS_TOKEN_SECRET,
        consumer_key = conf.CONSUMER_KEY,
        consumer_key_secret = conf.CONSUMER_KEY_SECRET,
        usernames = users_list,

        storage = dbs
    )

    te.download_tweets()

def delete_user(user_name):
    TwitterUser.objects.filter(screen_name=user_name).delete()
    print('Usuario eliminado satisfactoriamente de BD')

# user_name = 'Ninelconde'
# text = 'Tweet de prueba, verificar que es posible insertar un texto'
def add_text_user(user_name, text):
    if TwitterUser.objects.filter(screen_name=user_name).exists():
        user = TwitterUser.objects.get(screen_name=user_name)
        Tweet.objects.create(twitter_user=user, tweet_text=text, tweet_date=datetime.now(), tweet_lang='es', is_retweet=False)
        print(f"El texto del usuario '{user_name}', fue agregado satisfactoriamente en la DB")
    else:
        print("El usuario no existe en BD. Por favor inserte antes el usuario en BD")
# if __name__=='__main':
#     download_all_tweets_user(user)

#------------------------------------------TASKS--------------------------------------------
#Validate
def validate_model(list_prep: list, encoding: EncodingMethod, method: ClassificationMethod):
    if type_user.name == 'politicos'

#Classification.
#guardar modelos
#save model train in the file
dump(model, 'models/model_train.jb')
#load the model
model1 = load('models/model_train.jb')

def create_model():
    pass
def update_model():
    pass
def find_author():
    pass