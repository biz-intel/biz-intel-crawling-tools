
class twitter:

    def __init__(self, sntwitter, connection, key_word) -> None:
        self.sntwitter = sntwitter
        self.connection = connection
        self.connection.reset_count()
        self.key_word = key_word

    def start_download(self, *filters, date=None):
        query = self.key_word
        if date != None:
            query =query+ ' since:' +date
        if len(filters) > 0:
            for f in filters:
                query = query + ' -filter:'+f
        for tweet in self.sntwitter.TwitterSearchScraper(query).get_items():
            data = {}
            data['Холбоос'] = vars(tweet)['url'],
            data['Хэрэглэгчийн бүртгэлийн дугаар'] = vars(tweet)['user'].id,
            data['Жиргээ'] = vars(tweet)['content'],
            data['Нийтлэгдсэн огноо'] = str(vars(tweet)['date'])
            self.connection.build_data(data)
            self.connection.print_data()
        if self.connection.get_inserted() == 0:
            print('->           Жиргээ олдсонгүй...!')
        self.connection.insert_data(collection_name = self.query, key_word = "tweeter")
        # print('->           Татагдсан жиргээний тоо:', self.connection.get_counts()['inserted'])