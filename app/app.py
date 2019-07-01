from flask import Flask, request, render_template, flash
import mysql.connector
import os
from werkzeug.utils import secure_filename
import json

from worker import worker
from api import ApiClient

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html", title = "Homepage")

@app.route("/add-match", methods = ["GET", "POST"])
def add_match():
    if request.method == "GET":
        return render_template("add_match.html", title = "Upload a replay")
    elif request.method == "POST":
        file = request.files["file"]

        if file and file.filename != "":
            replay_id = request.form["replay_id"].strip()
            replay_filename = secure_filename(replay_id + ".dem")
            file.save(os.path.join("/app/replays", replay_filename))

            metadata = {
                "replay_id": replay_id,
                "radiant_team": request.form["radiant_team"],
                "dire_team": request.form["dire_team"] 
            }
            metadata_filename = secure_filename(replay_id + "_meta.json")

            with open(secure_filename(metadata_filename), "w") as f:
                json.dump(metadata, f)

            worker.send_task("tasks.parse_and_store", args = [replay_filename, metadata_filename])

            flash("Replay uploaded!")
            return render_template("add_match.html", title = "Upload a replay")

        else:
            flash("Error!")
            return render_template("add_match.html", title = "Upload a replay")

@app.route("/team/<team>")
def view_team(team: str):
    with ApiClient() as client:
        team = client.team_results(team)
        return render_template("team.html", title = team['name'], team = team)

@app.route("/player/<player>")
def view_player(player: str):
    with ApiClient() as client:
        player = client.player_results(player)
        return render_template("player.html", title = player['name'], player = player)

@app.route("match/<match_id>")
def view_match(match_id: int):
    with ApiClient() as client:
        match = client.match_results(match_id)
        return render_template("match.html", title = f"{match['radiant_team']} - {match['dire_team']}", match = match)