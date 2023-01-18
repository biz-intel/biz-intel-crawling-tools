
class twitter:

    def __init__(self, sntwitter, connection, key_word, strftime) -> None:
        self.sntwitter = sntwitter
        self.connection = connection
        self.connection.reset_count()
        self.query = key_word
        self.format = strftime

    def start_download(self, *filters, date=None):
        query = self.query
        if date != None:
            query =query+ ' since:' +date
        if len(filters) > 0:
            for f in filters:
                query = query + ' -filter:'+f
        tweets = self.sntwitter.TwitterSearchScraper(query).get_items()
        # if len(tweets) == 0:
        #     print('->           Жиргээ олдсонгүй...!')
        # else:
        for tweet in tweets:
            data = {
                'link' : str(vars(tweet)['url']),
                'user_name' : str(vars(tweet)['user'].username),
                'body' : str(vars(tweet)['content']),
                'created_date' : self.format(vars(tweet)['date'], "%Y-%m-%d"),
                'key_word' : self.query,
                'site' : 'tweeter'
                }
            self.connection.build_data(data)
            self.connection.insert_data()
            break
        if self.connection.get_inserted() == 0:
            print('->           Жиргээ олдсонгүй...!')