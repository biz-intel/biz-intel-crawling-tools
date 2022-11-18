import os
import sys
import time
import random
import datetime
import requests
from configs import main_configures

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from modules.linkedin                           import linkedin

from dotenv                                     import load_dotenv
from random                                     import randint
from datetime                                   import datetime
from datetime                                   import timedelta
from bs4                                        import BeautifulSoup
from selenium                                   import webdriver
from selenium.webdriver.common.by               import By
from ..assets.database                            import database
from selenium.webdriver.common.action_chains    import ActionChains
from selenium.common.exceptions                 import WebDriverException
from selenium.common.exceptions                 import StaleElementReferenceException

def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


load_dotenv()

db_connection = database('biz_intel_fourth_valution')

class linkedin_configs(main_configures):
    def __init__(self) -> None:
        super().__init__()
        self.configure_email('linkedin')
        self.configure_password('linkedin')

    def start(self):
        driver = webdriver.Chrome(options = self.options)
        action = ActionChains(driver)
        for key_word in self.key_words:
            print("*************************************************")
            print("->   Түлхүүр үг:", key_word)
            print("->   Эхэлсэн цаг:", get_time())
            scraper =  linkedin    ( 
                            query = key_word,
                            connection = db_connection,
                            driver = driver,
                            By = By,
                            bs4 = BeautifulSoup,
                            randint = random.randint,
                            requests = requests,
                            time = time,
                            exception = StaleElementReferenceException, 
                            action = action,
                            callback=None,
                            email=self.email,
                            password=self.pass_word,
                        ),
            scraper.start_download()
            time.sleep(randint(1, 4))
            print("->   Дууссан цаг:", get_time())
        driver.close()