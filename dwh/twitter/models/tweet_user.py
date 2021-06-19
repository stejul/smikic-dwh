from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import relationship

from dwh.twitter.models import Base


class TweetUser(Base):

    __tablename__ = "tweet_user"

    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    screen_name = Column(String)
    name = Column(String)
    twitter_id = Column(String)

    tweets = relationship("Tweet", backref="tweet_user", lazy=True)
