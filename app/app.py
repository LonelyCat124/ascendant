from flask import Flask, request, render_template
import mysql.connector
import os
from werkzeug.utils import secure_filename
import json

from worker import worker
from api import ApiClient

app = Flask(__name__)

@app.route("/")
def index():
    task = worker.send_task("tasks.add_to_db", args = ["test.dem"])
    return "Task queued!"

@app.route("/add-match", methods = ["GET", "POST"])
def add_match():
    if request.method == "GET":
        return render_template("add-match.html")
    elif request.method == "POST":
        file = request.files["file"]

        if file and file.filename != "":
            replay_id = request.form["replay_id"].strip()
            replay_filename = secure_filename(replay_id + ".dem")
            file.save(os.path.join("/app/replays", replay_filename))

            metadata = {
                "replay_id": replay_id,
                "radiant_team": request.form["radiant_team"]
                "dire_team": request.form["dire_team"] 
            }
            metadata_filename = secure_filename(replay_id + "_meta.json")

            with open(secure_filename(metadata_filename, "w") as f:
                json.dump(metadata, f)

            worker.send_task("tasks.parse_and_store", args = [replay_filename, metadata_filename])

            return "Replay uploaded!"

        else:
            return "Error"