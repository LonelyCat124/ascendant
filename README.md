# Ascendant
Ascendant is a Dota 2 inhouse league visualisation app. It uses OpenDota's [replay parser](https://github.com/odota/parser/) and provides an interface for viewing statistics from the parsed matches. 

Ascendant is designed to help casters and analysts who are part of a small / medium inhouse league. It's not set up to be a large scale automated replay parser, and it's unlikely to ever be. 

## Usage
Team captains upload match replays via the form on `/add-match`. This kicks off the replay parser and adds data from the match to the database.

Casters, analysts and players can then view match, player, hero and item statistics via the dashboard at `/dashboard`.

## Deployment
The whole app is launched via `docker-compose`, and the front-end is accessible on port [5000](http://localhost:5000).
```
docker-compose up
```
--TODO docker volume mounts
## Architecture
Ascendant is made up of 5 components:
* Web front-end (Python/Flask)
* Replay parser (OpenDota's Java parser)
* Database (MySQL)
* Task & message queue (Redis)
* Task worker (Python/Celery)

The front-end is the only component accessible outside the network.
Docker volumes are used to provide persistent storage for the uploaded replay files and database tables.

When the front-end recieves a replay file it saves the file to disk then kicks off a Celery task. It's this task that passes the file to the replay parser, formats the results and writes them to the DB. 