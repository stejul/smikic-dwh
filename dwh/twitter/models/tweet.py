from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from dwh.twitter.models import Base

class Tweet(Base):

    __tablename__ = "tweet"

    id = Column(BigInteger, primary_key=True, autoincrement="auto")
    text = Column(String)
    tweet_id = Column(String)
    created_at = Column(DateTime)

    user_id = Column(BigInteger, ForeignKey("tweet_user.id"), nullable=True)
    #tweeter_user = relationship("TweetUser")


