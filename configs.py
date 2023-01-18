import os
# import pymongo
import requests
from dotenv import load_dotenv
from selenium import webdriver

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

class database_configures:
    
    def __init__(self) -> None:
        load_dotenv()
        # self.myclient = pymongo.MongoClient("mongodb+srv://"+os.getenv(key = 'mongodb_username')+":"+os.getenv(key='mongodb_password')+
        #                                                     "@first-cluster.hmz4mpz.mongodb.net/?retryWrites=true&w=majority")
        # self.mydatabase = self.myclient["crawl"]
        self.inserted = 0
        self.tweet_inserted = 0
        self.tweet_updated = 0
        self.data = {}

    def get_inserted(self):
        return self.inserted

    def reset_count(self):
        self.inserted = 0
        self.tweet_inserted = 0
        self.tweet_updated = 0

    def build_data(self, data:dict):
        self.data = data
    
    def print_data(self):
        print(self.data)

    def insert_data(self):
        response = requests.post("https://api.biz-intel.tech/insert_data", data=self.data)
        print(response.text[:1000:])
        if response.text == "Inserted...!":
            self.inserted+=1