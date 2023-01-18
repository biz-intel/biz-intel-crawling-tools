import os
import sys
import time
from configs import main_configures
from configs import database_configures

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from modules.linkedin                           import linkedin

from dotenv                                     import load_dotenv
from random                                     import randint
from datetime                                   import datetime
from datetime                                   import timedelta
from selenium                                   import webdriver
from selenium.webdriver.common.by               import By
from selenium.webdriver.common.keys             import Keys

def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


load_dotenv()

db_connection = database_configures()

def format_date(post_created_date:str)->str:
    def replace(created_date, char)->int:
        return int(created_date.replace(char, ""))
    if "m" in post_created_date:
        days = replace(post_created_date, "m") // 60//24
    elif "h" in post_created_date:
        days = replace(post_created_date, "h") // 60
    elif "d" in post_created_date:
        days = replace(post_created_date, "d") 
    elif "w" in post_created_date:
        days = replace(post_created_date, "w") * 7
    elif "mo" in post_created_date:
        days = replace(post_created_date, "mo") * 30
    else:
        days = replace(post_created_date, "yr") * 365
    created_at = datetime.now()-timedelta(days=days)
    return datetime.strftime(created_at, "%Y-%m-%d")
    


class linkedin_configs(main_configures):
    def __init__(self) -> None:
        super().__init__()
        self.configure_email('linkedin')
        self.configure_password('linkedin')

    def start(self, key_word):
        driver = webdriver.Chrome(options = self.options)
        print("*************************************************")
        print("->   Түлхүүр үг:", key_word)
        print("->   Эхэлсэн цаг:", get_time())
        scraper =  linkedin    ( 
                        query = key_word,
                        connection = db_connection,
                        driver = driver,
                        By=By,
                        time = time,
                        callback=format_date,
                        Key=Keys,
                        email=self.linkedin_email,
                        pass_word=self.linkedin_password,
                        randint=randint
                    )
        scraper.start_download()
        time.sleep(randint(1, 4))
        print("->   Дууссан цаг:", get_time())
        driver.close()
        driver.quit()
    def run(self):
        for key_word in self.key_words:
            self.start(key_word=key_word)