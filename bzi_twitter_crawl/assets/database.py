from configs import database_configures
class database(database_configures):

    def __init__(self, table_name) -> None:
        super().__init__()
        self.data
        self.table_name = table_name
        self.inserted = 0
        self.duplicated = 0

    def get_counts(self):
        return {'inserted':self.inserted, 'duplicated':self.duplicated}

    def reset_counts(self):
        self.inserted = 0
        self.duplicated = 0

    def insert(self, table_name, user_id, tweet_link, tweet_text, key_word, tweeted_date):
        sql = "INSERT INTO "+table_name+" (user_id, tweet_link, tweet_text, key_word, tweeted_date) VALUES (%s, %s, %s, %s, %s)"
        val = [ user_id, tweet_link, tweet_text, key_word, tweeted_date]
        try:
            super().commit(sql, val)
            self.inserted += 1
        except super().database_error:
            self.duplicated += 1