import os
import time
from database                       import database
from selenium.webdriver.common.by   import By
from selenium.webdriver.common.keys import Keys
from random                         import randint
from linkedin                       import linkedin
from datetime                       import datetime
from dotenv                         import load_dotenv
from selenium                       import webdriver
from datetime                       import timedelta
load_dotenv()

class main_configures:
    def __init__(self) -> None:
        load_dotenv()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--headless")
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        key_words = os.getenv('key_words').split(sep=(','))
        self.key_words = []
        for key in key_words:
            self.key_words.append(key.strip())
        self.linkedin_email = os.getenv(key='linkedin_email')
        self.linkedin_password = os.getenv(key='linkedin_password')
        
    def configure_email(self, type:str):
        self.email = os.getenv(type+'_email')
    
    def configure_password(self, type:str):
        self.pass_word = os.getenv(type+'_password')

db_connection = database()

def get_time()->str:
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

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
    return datetime.strftime(created_at, "%Y")
    


class linkedin_configs(main_configures):
    def __init__(self) -> None:
        super().__init__()
        self.configure_email('linkedin')
        self.configure_password('linkedin')

    def start(self):
        driver = webdriver.Chrome(options = self.options)
        for key_word in self.key_words:
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
        self.start()