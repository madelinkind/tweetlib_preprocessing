import os
import sys

FILE = __file__
DATA_SET_FOLDER = os.path.split(FILE)[0]
TWEET_LIB_FOLDER = os.path.split(DATA_SET_FOLDER)[0]
PROJECT_FOLDER = os.path.split(TWEET_LIB_FOLDER)[0]

sys.path.append(PROJECT_FOLDER)

from tweetlib.definitions import TypeUser
from tweetlib.data_set.data_set import DataSet

class DataSetPoliticos(DataSet):

#dame la instancia padre e invocale el constructor con este parametro
    def __init__(self, *args, **kwargs):
        super(DataSetPoliticos, self).__init__(TypeUser.politico)
