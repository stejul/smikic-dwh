import sys
from dwh.twitter.listener import Listener as TwitterListener

from dotenv import load_dotenv
from tweepy import Stream, OAuthHandler


import os
import time
import logging

logging.basicConfig(
    filename="dwh/app.log",
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s",
)


class TwitterStream:

    load_dotenv()

    TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
    TWITTER_CONSUMER_KEY_SECRET = os.getenv("TWITTER_CONSUMER_KEY_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    def periodicWork(self, interval):
        listener = TwitterListener()
        auth = OAuthHandler(self.TWITTER_CONSUMER_KEY, self.TWITTER_CONSUMER_KEY_SECRET)
        auth.set_access_token(
            self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET
        )

        stream = Stream(auth, listener)
        logging.info("starting twitter data science stream")
        while True:
            stream.filter(track=["Data Science"])
            time.sleep(interval)


if __name__ == "__main__":
    object = TwitterStream()
    object.periodicWork(60 * 0.1)
