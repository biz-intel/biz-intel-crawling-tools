
class twitter:

    def __init__(self, sntwitter, connection, key_word) -> None:
        self.sntwitter = sntwitter
        self.connection = connection
        self.connection.reset_count()
        self.query = key_word

    def start_download(self, *filters, date=None):
        query = self.query
        if date != None:
            query =query+ ' since:' +date
        if len(filters) > 0:
            for f in filters:
                query = query + ' -filter:'+f
        for tweet in self.sntwitter.TwitterSearchScraper(query).get_items():
            data = {
                'link' : str(vars(tweet)['url']),
                'user_name' : str(vars(tweet)['username']),
                'body' : str(vars(tweet)['rawContent']),
                'created_date' : str(vars(tweet)['date']),
                'key_word' : self.query,
                'site' : 'tweeter'
                }
            self.connection.build_data(data)
            self.connection.insert_data()
        if self.connection.get_inserted() == 0:
            print('->           Жиргээ олдсонгүй...!')
        else:
            self.connection.insert_data()
            print('->           Татагдсан жиргээний тоо:', self.connection.get_inserted())