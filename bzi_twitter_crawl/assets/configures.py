import os
import sys
from configs import main_configures
from configs import database_configures

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import snscrape.modules.twitter as sntwitter
from datetime                   import datetime
from modules.twitter            import twitter

def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

connection = database_configures()

class twitter_configs(main_configures):
    def __init__(self) -> None:
        super().__init__()

    def start(self):        
        print("*************************************************")
        print('->   Жиргээнүүдийг татаж эхэлж байна')
        print('->   Эхэлсэн цаг:', get_time())

        for key_word in self.key_words:
            print('->       Түлхүүр үг:', key_word)
            twitter(sntwitter=sntwitter, connection=connection, key_word=key_word).start_download('replies','retweets', date='2023-01-01')

        print('->   Дууссан цаг:', get_time())

    def run(self):
        self.start()