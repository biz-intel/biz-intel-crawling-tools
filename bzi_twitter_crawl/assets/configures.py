import os
import sys
from configs import main_configures
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import snscrape.modules.twitter as sntwitter

from assets.database          import database
from datetime                   import datetime
from modules.twitter            import twitter

def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

connection = database(table_name='tweets_2022_valute')

class twitter_configs(main_configures):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        print('->   Жиргээнүүдийг татаж эхэлж байна')
        print('->   Эхэлсэн цаг:', get_time())

        for key_word in super().key_words:
            print('->       Түлхүүр үг:', key_word)
            twitter(sntwitter=sntwitter, connection=connection, key_word=key_word).start_download('replies','retweets', date='2022-01-01')

        print('->   Дууссан цаг:', get_time())

    def run(self):
        self.start()