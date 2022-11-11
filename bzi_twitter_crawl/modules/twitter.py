class twitter:

    def __init__(self, sntwitter, connection, key_word) -> None:
        self.sntwitter = sntwitter
        self.connection = connection
        self.connection.reset_counts()
        self.key_word = key_word

    def start_download(self, *filters, date=None):
        query = self.key_word
        if date != None:
            query =query+ ' since:' +date
        if len(filters) > 0:
            for f in filters:
                query = query + ' -filter:'+f
        for tweet in self.sntwitter.TwitterSearchScraper(query).get_items():
            pass
            # self.connection.insert_tweets(vars(tweet)['user'].id, vars(tweet)['url'], vars(tweet)['content'], self.key_word, str(vars(tweet)['date']))
        print('->           Татагдсан жиргээний тоо:', self.connection.get_counts()['inserted'])
        print('->           Давхардсан жиргээний тоо:', self.connection.get_counts()['duplicated'])