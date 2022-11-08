import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import mysql.connector as connector
from dotenv import load_dotenv
import snscrape.modules.twitter as sntwitter
from database import database
from modules.twitter import twitter
from datetime import datetime

load_dotenv()

queries = os.getenv('key_words').split(' ')

my_connector = connector.connect(
    host     = os.getenv('host'),
    user     = os.getenv('user_name'),
    password = os.getenv('password'),
    database = os.getenv('database'),
)

connection = database(connector=my_connector, DatabaseError=connector.DatabaseError, table_name='tweets_2022_valute')

def start():
    print('Жиргээнүүдийг татаж эхэлж байна, эхэлсэн огноо:', datetime.now())
    for key_word in queries:
        print('->   Түлхүүр үг:', key_word)
        twitter(sntwitter=sntwitter, connection=connection, key_word=key_word).start_download('replies','retweets', date='2022-01-01')
        print('->       Амжилттай дууслаа...')

class twitter_configs:

    def run(self):
        start()