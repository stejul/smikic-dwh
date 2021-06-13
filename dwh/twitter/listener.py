from tweepy import StreamListener
from kafka import KafkaProducer

class Listener(StreamListener):

    try:
        producer = KafkaProducer(bootstrap_servers="broker:9092")
    except:
        pass
    TOPIC_NAME = "dataScience"

    def on_data(self, data):
        self.producer.send(self.TOPIC_NAME, data.encode("utf-8"))
        print(data)
        return True

    def on_error(self, status):
        print(status)
    
    def getTopicName(self):
        return self.TOPIC_NAME
