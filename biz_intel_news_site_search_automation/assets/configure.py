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

from random                                     import randint
from datetime                                   import datetime
from bs4                                        import BeautifulSoup
from selenium                                   import webdriver
from selenium.webdriver.common.by               import By
from assets.database                            import database
from selenium.webdriver.common.action_chains    import ActionChains
from mysql.connector.errors                     import IntegrityError
from selenium.common.exceptions                 import WebDriverException
from selenium.common.exceptions                 import StaleElementReferenceException



os.environ['PATH'] = r"C:\Assets"

db_connection = database(host_name = 'localhost', user_name = 'root', user_password = '', database_name = 'news', table_name = 'biz_intel_fourth_valution', mysql_connector = connector, integrity_error = IntegrityError)

def start(queries:list):
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
                        action = None
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
                        action = None
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
                        action = None
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
                        action=None,
                    ),
                    ]
        for scraper in scrapers:
            scraper.start_download()
            time.sleep(randint(1, 4))
        print("->   Дууссан цаг:", datetime.now())
    driver.close()