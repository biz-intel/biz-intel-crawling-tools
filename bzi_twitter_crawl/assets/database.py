class database:

    def __init__(self, connector, DatabaseError, table_name) -> None:
        self.connector = connector
        self.DatabaseError = DatabaseError
        self.table_name = table_name
        self.cursor = self.connector.cursor()
        self.inserted = 0
        self.duplicated = 0

    def get_counts(self):
        return {'inserted':self.inserted, 'duplicated':self.duplicated}

    def reset_counts(self):
        self.inserted = 0
        self.duplicated = 0

    def commit(self, sql, val):
        self.cursor.execute(sql, val)
        self.connection.commit()

    def insert(self, table_name, user_id, tweet_link, tweet_text, key_word, tweeted_date):
        sql = "INSERT INTO "+table_name+" (user_id, tweet_link, tweet_text, key_word, tweeted_date) VALUES (%s, %s, %s, %s, %s)"
        val = [ user_id, tweet_link, tweet_text, key_word, tweeted_date]
        try:
            self.commit(sql, val)
            self.inserted += 1
        except self.DatabaseError:
            self.duplicated += 1