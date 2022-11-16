import os
import mysql.connector as connector
from dotenv import load_dotenv
from selenium import webdriver
from mysql.connector.errors import IntegrityError
from mysql.connector.errors import DatabaseError

load_dotenv()

class main_configures:

    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.key_words = os.getenv('key_words').split(sep=(','))

class database_configures:
    
    def __init__(self) -> None:
        self.connection = connector.connect(host = os.getenv('database_host'), user = os.getenv('database_username'), password = os.getenv('database_password'), database = os.getenv('database_name'))
        self.cursor = self.connection.cursor()
        self.error = IntegrityError
        self.database_error = DatabaseError

    def commit(self, sql, val):
        self.cursor.execute(sql, val)
        self.connection.commit()