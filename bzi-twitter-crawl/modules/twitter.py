import snscrape.modules.twitter as sntwitter
import mysql.connector

my_connector = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="tweets"
)
mycursor = my_connector.cursor()

sql = "INSERT INTO usdTweets (user_id, tweet_link, tweet_text, key_word, tweeted_date) VALUES (%s, %s, %s, %s, %s)"

# key_words = ['доллар', 'долларын', 'ханш', 'ханшны', 'ханшийн', 'эдийн засаг', 'эдийн засгийн', 'хил', 'бензин', 'бензиний', 'үнэ', 'үнийн', 'валют', 'валютын']
key_words = ['долларын', 'ханш', 'ханшны', 'ханшийн', 'эдийн засаг', 'эдийн засгийн', 'хил', 'бензин', 'бензиний', 'үнэ', 'үнийн', 'валют', 'валютын']

for key_word in key_words:
    query = key_word + ' since:2022-01-01 -filter:replies -filter:retweets'
    inserted = 0
    duplicate = 0
    print('Downloading....!')
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        try:
            val = (vars(tweet)['user'].id, vars(tweet)['url'], vars(tweet)['content'], key_word, str(vars(tweet)['date']))
            mycursor.execute(sql, val)
            my_connector.commit()
            inserted += 1
        except mysql.connector.DatabaseError as error:
            duplicate += 1
    print("*****************************************************************************")
    print('Inserted:', inserted)
    print('Duplicate errored:', duplicate)
    print('Done...!')
    print('Keyword:', key_word)

    class twitter:

        def __init__(self) -> None:
            pass