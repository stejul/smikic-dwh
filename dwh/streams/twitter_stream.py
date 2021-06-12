import sys
#sys.path.append("./listener.py")
from dwh.streams.listener import TwitterListener

from dotenv import load_dotenv
from tweepy import Stream, OAuthHandler


import os
import time

class TwitterStream():

    load_dotenv()

    TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
    TWITTER_CONSUMER_KEY_SECRET = os.getenv("TWITTER_CONSUMER_KEY_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    def periodicWork(self, interval):
        listener = TwitterListener()
        auth = OAuthHandler(self.TWITTER_CONSUMER_KEY, self.TWITTER_CONSUMER_KEY_SECRET)
        auth.set_access_token(self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        while True:
            stream.filter(track=["Data Science"])
            time.sleep(interval)

if __name__ == "__main__":
    object = TwitterStream()
    object.periodicWork(60*0.1)
    
