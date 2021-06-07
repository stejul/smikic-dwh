from dotenv import load_dotenv
from kafka import KafkaProducer
from tweepy import Stream, StreamListener, OAuthHandler

import os
import time

load_dotenv()

TWITTER_CONSUMER_KEY= os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_KEY_SECRET = os.getenv("TWITTER_CONSUMER_KEY_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_URL = "https://api.twitter.com/2/tweets/search/stream"


class TwitterStreamListener(StreamListener):
    def on_data(self, data):
        producer.send("dataScience", data.encode("utf-8"))
        print(data)
        return True
    def on_error(self, status):
        print(status)

producer = KafkaProducer(bootstrap_servers="broker:9092")
listener = TwitterStreamListener()

auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

stream = Stream(auth, listener)

def periodicWork(interval):
    while True:
        #stream.filter(track=["Data Science"])
        stream.sample()
        time.sleep(interval)

periodicWork(60 * 0.1)
