from dwh.twitter.etl.extract_data import ExtractData
from luigi import Task, LocalTarget, run
import pandas as pd

class TransformData(Task):

    def requires(self):
        return [ExtractData()]

    def output(self):
        return LocalTarget("dwh/twitter/etl/dump/transformedData.csv")
    
    def run(self):
        #created_at, text, id
        df = pd.read_json("dwh/twitter/etl/dump/MongoDB_output.json", encoding="utf-8")

        #description, screen_name, id, name
        user = pd.json_normalize(df["user"])

        user_tweet = user[["id", "name", "screen_name", "description"]]
        tweet = df[["id", "text", "created_at"]]
        merged_df = pd.concat([user_tweet.add_suffix("_user"), tweet.add_suffix("_tweet")], axis=1)

        outfile = open(self.output().path, "wb") 
        merged_df.to_csv(outfile, encoding="utf-8",index=False)

if __name__ == "__main__":
    run(main_task_cls=TransformData, local_scheduler=False)
