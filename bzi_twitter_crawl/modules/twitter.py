
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
                'Холбоос' : str(vars(tweet)['url']),
                'Хэрэглэгчийн бүртгэлийн дугаар' : str(vars(tweet)['user'].id),
                'Жиргээ' : str(vars(tweet)['content']),
                'Нийтлэгдсэн огноо' : str(vars(tweet)['date'])
                }
            self.connection.build_data(data)
        if self.connection.get_inserted() == 0:
            print('->           Жиргээ олдсонгүй...!')
        else:
            self.connection.insert_data(collection_name = self.query, key_word = "twitter")
            print('->           Татагдсан жиргээний тоо:', self.connection.get_inserted())