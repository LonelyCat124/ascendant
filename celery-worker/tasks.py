from celery import Celery
from replay_summary import ReplaySummariser

import time
import requests
import json

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name = "tasks.parse_and_store")
def parse_and_store(replay_file: str, metadata_file: str) -> bool:
    # Load metadata
    with open(metadata_file, "r") as meta:
        metadata = json.load(meta)

    # send the file to the parser
    with open(replay_file, "rb") as replay:
        r = requests.post("http://parser:5600", files = {"file": replay})

    parsed_replay = r.json()

    # save the response before messing with it
    with open(metadata.replay_id + "_parsed.json", "w") as response:
        json.dump(parsed_replay, response)

    # extract match data from the parsed replay
    rs = ReplaySummariser(parsed_replay)

    # send to DB table
    with DbClient(rs) as dbc:
        dbc.insert()
    
    return True