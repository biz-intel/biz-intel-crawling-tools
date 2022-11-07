class database:

    def __init__(self, connector, DatabaseError, table_name) -> None:
        self.connector = connector
        self.DatabaseError = DatabaseError
        self.table_name = table_name
        self.cursor = self.connector.cursor()

    def insert(self, table_name):
        sql = "INSERT INTO "+table_name+" (user_id, tweet_link, tweet_text, key_word, tweeted_date) VALUES (%s, %s, %s, %s, %s)"