import os
import time
import random
import requests
import mysql.connector as connector

from modules.gogo                               import gogo
from modules.ikon                               import ikon
from modules.isee                               import isee
from modules.medee                              import medee
from modules.news                               import news
from modules.sonin                              import sonin
from modules.updown                             import updown
from modules.zindaa                             import zindaa

from dotenv                                     import load_dotenv
from random                                     import randint
from datetime                                   import datetime
from datetime                                   import timedelta
from bs4                                        import BeautifulSoup
from selenium                                   import webdriver
from selenium.webdriver.common.by               import By
from assets.database                            import database
from selenium.webdriver.common.action_chains    import ActionChains
from mysql.connector.errors                     import IntegrityError
from selenium.common.exceptions                 import WebDriverException
from selenium.common.exceptions                 import StaleElementReferenceException

os.environ['PATH'] = r"".join('./assets/')


load_dotenv()

db_connection = database(
                    host_name       =   os.getenv('host'),
                    user_name       =   os.getenv('user_name'),
                    user_password   =   os.getenv('password'),
                    database_name   =   os.getenv('database'),
                    table_name      =   'biz_intel_fourth_valution',
                    mysql_connector = connector,
                    integrity_error = IntegrityError
                    )

queries = os.getenv('key_words').split(sep=(','))
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

def start():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    driver = webdriver.Chrome(options = options)
    action = ActionChains(driver)
    for query in queries:
        print("*************************************************")
        print("->   Түлхүүр үг:", query)
        print("->   Эхэлсэн цаг:", datetime.now())
        scrapers =  [
            gogo    ( 
                        query = query,
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
                        query = query,
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
                        query = query,
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
                        query = query,
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
                        query = query,
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
                        query = query,
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
                        query = query,
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
                        query = query,
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

class configs:
    
    def run(self):
        start()