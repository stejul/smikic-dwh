
# Smikic DWH

It's a personal Data Warehouse to test out different APIs and Tools like:
- Kafka
- Luigi
- Docker
- Mongo and PostgreSQL


## What the Project does

- Perform ETL tasks with Luigi
- Kafka Streams for the Twitter Stream API
- MongoDB as a Archive
- PostgreSQL for the transformed Data
- Generate docker environment dynamically
  
## Tech Stack

- Kafka
- MongoDB
- PostgreSQL
- Python
    - Jinja2
    - Kafka wrapper
    - Luigi
    - PyMongo
    - SQLAlchemy
    - Tweepy
  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`POSTGRES_HOST`

`POSTGRES_DB`

`TWITTER_CONSUMER_KEY`

`TWITTER_CONSUMER_KEY_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_TOKEN_SECRET`

## Installation 

To install the project either use `pip` or `poetry`

```bash 
    pip install -r requirements.txt
```
or
```bash 
    poetry install
```

## Authors

- [@stejul](https://www.github.com/stejul)

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/stejul/smikic-dwh
```

Generate docker environment

```bash
  python dwh/utils/create_docker_environment.py
```

Start the docker environment

```bash
  docker-compose up
```

  
## License

[MIT](https://github.com/stejul/smikic-dwh/blob/main/LICENSE)

  
## Acknowledgements

 - [I wanna thank me](https://www.youtube.com/watch?v=c-Pv55i2bc0)
 - [I wanna thank me for believing in me](https://www.youtube.com/watch?v=c-Pv55i2bc0)

  
