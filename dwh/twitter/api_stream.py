from dotenv import load_dotenv
from kafka import KafkaConsumer, KafkaProducer
import os

load_dotenv()

TWITTER_BEARER = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_URL = "https://api.twitter.com/2/tweets/search/stream"


producer = KafkaProducer(bootstrap_server="localhost:9092")
topic_name = "get-twitter-stream"
