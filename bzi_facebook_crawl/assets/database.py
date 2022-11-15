class database:

    def __init__(self, host_name:str, user_name:str, user_password:str, database_name:str, table_name:str, mysql_connector, integrity_error) -> None:
        self.connector = mysql_connector
        self.connection = self.connector.connect(host = host_name, user = user_name, password = user_password, database = database_name)
        self.cursor = self.connection.cursor()
        self.table_name = table_name
        self.key_types = ['title', 'img', 'body', 'site']
        self.inserted = 0
        self.error = integrity_error

    def commit(self, sql, val):
        self.cursor.execute(sql, val)
        self.connection.commit()

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