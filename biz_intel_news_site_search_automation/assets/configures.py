import os
import sys
import time
import random
import datetime
import requests
import threading

from configs import main_configures
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from modules.gogo                               import gogo
from modules.ikon                               import ikon
from modules.isee                               import isee
from modules.medee                              import medee
from modules.news                               import news
from modules.sonin                              import sonin
from modules.updown                             import updown
from modules.zindaa                             import zindaa

from random                                     import randint
from datetime                                   import datetime
from datetime                                   import timedelta
from bs4                                        import BeautifulSoup
from selenium                                   import webdriver
from selenium.webdriver.common.by               import By
from ..assets.database                            import database
from selenium.webdriver.common.action_chains    import ActionChains
from mysql.connector.errors                     import IntegrityError
from selenium.common.exceptions                 import WebDriverException
from selenium.common.exceptions                 import StaleElementReferenceException

db_connection = database(table_name = 'biz_intel_fourth_valution')

def format_date(news_created)->str:
    news_created = news_created.lower()
    if news_created[1] ==' ':
        news_created = '0' + news_created
    if 'өчигдөр' in news_created:
        news_created = datetime.now()-timedelta(days=1)
    elif 'минутын' in news_created:
        news_created = datetime.now()-timedelta(minutes=int(news_created[:2:]))
    elif 'цагийн' in news_created:
        news_created = datetime.now()-timedelta(hours=int(news_created[:2:]))
    elif 'өдрийн' in news_created:
        news_created = datetime.now()-timedelta(days=int(news_created[:2:]))
    try:
        news_created = datetime.strftime(news_created, '%Y-%m-%d')
    except ValueError:
        news_created = datetime.strftime(news_created, '%Y.%m.%d')
    except TypeError:
        try:
            news_created = datetime.strftime(datetime.strptime(news_created, '%Y-%m-%d %H:%M'), '%Y-%m-%d')
        except ValueError:
            try:
                news_created = datetime.strftime(datetime.strptime(news_created, '%Y-%m-%d'), '%Y-%m-%d')
            except ValueError:
                news_created = datetime.strftime(datetime.strptime(news_created, '%Y.%m.%d'), '%Y.%m.%d')
    return news_created

class news_configs(main_configures):
    def __init__(self) -> None:
        super().__init__()

    def start(self, key_word):
        driver = webdriver.Chrome(options = self.options)
        action = ActionChains(driver)
        
        print("*************************************************")
        print("->   Түлхүүр үг:", key_word)
        print("->   Эхэлсэн цаг:", datetime.now())

        scrapers =  [
                gogo    ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = None, 
                            action = action,
                            callback = format_date
                        ),
                ikon    ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = StaleElementReferenceException,
                            action = None,
                            callback = format_date
                        ),
                isee    ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = WebDriverException,  
                            action = action,
                            callback = format_date
                        ),
                medee   ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = WebDriverException, 
                            action = action,
                            callback = format_date
                        ),
                news    ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = StaleElementReferenceException,
                            action = None,
                            callback = format_date
                        ),
                sonin   ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = StaleElementReferenceException,
                            action = None,
                            callback = format_date
                        ),
                updown  ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = WebDriverException, 
                            action = action,
                            callback = format_date
                        ),
                zindaa  ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = WebDriverException,
                            action = None,
                            callback = format_date
                    ),
                ]
        
        for scraper in scrapers:
            scraper.start_download()
            time.sleep(randint(1, 4))
        
        print("->   Дууссан цаг:", datetime.now())
        driver.close()

    def run(self):
        for key_word in self.key_words:
            self.start(key_word)