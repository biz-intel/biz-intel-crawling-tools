import os
import mysql.connector as connector
from dotenv import load_dotenv
from selenium import webdriver
from mysql.connector.errors import IntegrityError
from mysql.connector.errors import DatabaseError

class main_configures:

    def __init__(self) -> None:
        load_dotenv()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        key_words = os.getenv('key_words').split(sep=(','))
        self.key_words = []
        for key in key_words:
            self.key_words.append(key.strip())
        self.email = ''
        self.pass_word = ''
    def configure_email(self, type:str):
        self.email = os.getenv(type+'_email')
    
    def configure_password(self, type:str):
        self.pass_word = os.getenv(type+'_password')

class database_configures:
    
    def __init__(self) -> None:
        load_dotenv()
        self.connection = connector.connect(
                                            host=os.getenv(key='database_host'),
                                            username=os.getenv(key='database_username'),
                                            password=os.getenv(key='database_password'),
                                            database=os.getenv(key='database_name'),
                                            )
        self.cursor = self.connection.cursor()
        self.error = IntegrityError
        self.database_error = DatabaseError

    def commit(self, sql, val):
        self.cursor.execute(sql, val)
        self.connection.commit()