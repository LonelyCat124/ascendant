from celery import Celery
import time

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name = "tasks.add_to_db")
def add_to_db(filename: str) -> bool:
    # send the file to the parser

    # parse the returned json

    # send to DB table
    time.sleep(2)
    return True