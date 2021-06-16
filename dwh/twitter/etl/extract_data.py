from luigi import Task, LocalTarget, run
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
from bson.json_util import dumps

import os
import logging


class ExtractData(Task):
    load_dotenv()
    logging.basicConfig(filename="dwh/app.log", filemode="a", format="%(name)s - %(levelname)s - %(message)s")
    
    def requires(self)->None:
        return []

    def output(self):
        return LocalTarget("dwh/twitter/etl/dump/MongoDB_output.json")

    def run(self):
        DB_USER = os.getenv("POSTGRES_USER")
        DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

        #Connect to database and collection
        client = MongoClient(host=["localhost:27017"], username=quote_plus(DB_USER), password=quote_plus(DB_PASSWORD))
        db = client["dwh"]
        collection = db["sink"]

        result = []
        #iterate through every single entry
        for entry in collection.find():
            result.append(entry)

        f = self.output().open("w")
        #save result as json dump to output
        print(dumps(result, indent=2), file=f)
        f.close()

        logging.info("connecting to database")

if __name__ == "__main__":
    run(main_task_cls=ExtractData, local_scheduler=False)
