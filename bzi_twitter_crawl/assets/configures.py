import os

import mysql.connector          as connector
import snscrape.modules.twitter as sntwitter

from dotenv                     import load_dotenv
from database                   import database
from datetime                   import datetime
from modules.twitter            import twitter

load_dotenv()

queries = os.getenv('key_words').split(',')

my_connector = connector.connect(
    host     = os.getenv('host'),
    user     = os.getenv('user_name'),
    password = os.getenv('password'),
    database = os.getenv('database'),
)
def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

connection = database(connector=my_connector, DatabaseError=connector.DatabaseError, table_name='tweets_2022_valute')

def start():
    print('->   Жиргээнүүдийг татаж эхэлж байна')
    print('->   Эхэлсэн цаг:', get_time())

    for key_word in queries:
        print('->       Түлхүүр үг:', key_word)
        twitter(sntwitter=sntwitter, connection=connection, key_word=key_word).start_download('replies','retweets', date='2022-01-01')

    print('->   Дууссан цаг:', get_time())

class configs:

    def run(self):
        start()