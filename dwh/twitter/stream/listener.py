from tweepy import StreamListener
from kafka import KafkaProducer

class TwitterListener(StreamListener):

    producer = KafkaProducer(bootstrap_servers="broker:9092")
    TOPIC_NAME = "dataScience"

    def on_data(self, data):
        self.producer.send(self.TOPIC_NAME, data.encode("utf-8"))
        print(data)
        return True

    def on_error(self, status):
        print(status)
