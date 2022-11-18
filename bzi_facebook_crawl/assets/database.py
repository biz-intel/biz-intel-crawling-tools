from configs import database_configures
class database(database_configures):

    def __init__(self, table_name:str) -> None:
        super().__init__()
        self.table_name = table_name
        self.inserted = 0

    def get_inserted(self):
        return self.inserted

    def reset_count(self):
        self.inserted = 0

    def insert_data(self, title:str, img:str, body:str, site:str, link:str, key_word:str, news_created:str):
        try:
            sql = 'insert into '+self.table_name+'(title, img, body, site, link, key_word, news_created_date)values(%s,%s,%s,%s,%s, %s, %s)'
            val = [title, img, body, site, link, key_word, news_created]
            self.commit(sql = sql, val = val)
            self.inserted += 1
        except self.error:
            pass

    def insert_error_logs(self, site:str, key_word:str, error:str):
        try:
            sql = 'insert into error_logs(site, key_word, error)values(%s, %s, %s)'
            val = [site, key_word, error]
            self.commit(sql = sql, val = val)
        except self.error:
            pass

    def insert_count_logs(self, site:str, key_word:str):
        try:
            sql = 'insert into count_logs(site, key_word, inserted)values(%s, %s, %s)'
            val = [site, key_word, str(self.inserted)]
            self.commit(sql = sql, val = val)
        except self.error:
            pass

    def update_data(self, link:str, **kwargs):
        for column_name in kwargs:
            if column_name in self.key_types:
                sql = 'update ' +self.table_name +' set '+column_name+' = %s where link = %s'
                val = [kwargs[column_name], link]
                self.commit(sql = sql, val = val)