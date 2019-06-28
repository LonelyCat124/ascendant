from flask import Flask
import mysql.connector
from worker import worker
from api import ApiClient

app = Flask(__name__)

@app.route("/")
def index():
    task = worker.send_task("tasks.add_to_db", args = ["test.dem"])
    return "Task queued!"