import os
import sys
import time
import random
import datetime
import requests
import mysql.connector as connector

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from modules.facebook                           import facebook

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

def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

os.environ['PATH'] = r"".join('./assets/')


load_dotenv()

db_connection = database(
                    host_name       =   os.getenv('database_host'),
                    user_name       =   os.getenv('database_username'),
                    user_password   =   os.getenv('database_password'),
                    database_name   =   os.getenv('database_name'),
                    table_name      =   'biz_intel_fourth_valution',
                    mysql_connector = connector,
                    integrity_error = IntegrityError
                    )

queries = os.getenv('key_words').split(sep=(','))

def start():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',['enable-logging'])
    driver = webdriver.Chrome(options = options)
    action = ActionChains(driver)
    for query in queries:
        print("*************************************************")
        print("->   Түлхүүр үг:", query)
        print("->   Эхэлсэн цаг:", datetime.now())
        scraper =  facebook    ( 
                        query = query,
                        connection = db_connection,
                        driver = driver,
                        By = By,
                        bs4 = BeautifulSoup,
                        randint = random.randint,
                        requests = requests,
                        time = time,
                        exception = None, 
                        action = action
                    ),
        scraper.start_download()
        time.sleep(randint(1, 4))
        print("->   Дууссан цаг:", datetime.now())
    driver.close()


class facebook_configs:

    def run(self):
        pass