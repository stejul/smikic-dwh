from dwh.twitter.etl.transform_data import TransformData

from luigi import Task, run

from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session 

from dotenv import load_dotenv

from dwh.twitter.models.tweet import Tweet
from dwh.twitter.models.tweet_user import TweetUser
from dwh.twitter.models import Base


import pandas as pd
import os

class LoadDataInDwh(Task):
    load_dotenv()

    def requires(self):
        return [TransformData()]

    def output(self):
        return []

    def run(self):

        DB_USER = os.getenv("POSTGRES_USER")
        DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        DB_NAME = os.getenv("POSTGRES_DB")

        df = pd.read_csv("dwh/twitter/etl/dump/transformedData.csv")

        engine = create_engine(f"postgresql://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}@localhost/{quote_plus(DB_NAME)}")

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        session = Session(bind=engine)

        for idx, entry in df.iterrows():

            user=TweetUser(screen_name=entry["screen_name_user"],
                    name=entry["name_user"],
                    twitter_id = entry["id_user"])

            tweet = Tweet(text=entry["text_tweet"],
                        tweet_id=entry["id_tweet"],
                        created_at=entry["created_at_tweet"])

            tweet.tweet_user=user
            
            session.add(user)
            
            session.add(tweet)

        session.commit()

if __name__ == "__main__":
    run(main_task_cls=LoadDataInDwh, local_scheduler=False)
