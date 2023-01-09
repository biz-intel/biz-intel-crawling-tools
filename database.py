import pymongo
from dotenv import load_dotenv
class database:
    
    def __init__(self) -> None:
        load_dotenv()
        # self.myclient = pymongo.MongoClient("mongodb+srv://"+os.getenv(key = 'mongodb_username')+":"+os.getenv(key='mongodb_password')+
        #                                                     "@first-cluster.hmz4mpz.mongodb.net/?retryWrites=true&w=majority")
        # self.mydatabase = self.myclient["crawl"]
        self.inserted = 0
        self.datas = []

    def get_inserted(self):
        return self.inserted

    def reset_count(self):
        self.inserted = 0

    def build_data(self, data:dict):
        self.datas.append(data)
        self.inserted += 1
    
    def print_data(self):
        print(self.datas)

    def insert_data(self, collection:str, key_word:str):
        mycollection = self.mydatabase[collection]
        return mycollection.insert_one({key_word : self.datas})