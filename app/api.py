import mysql.connector
from typing import List, Dict, Any

Result = Dict[str, Any]
class ApiClient():
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'ascendant',
            'auth_plugin': 'mysql_native_password'
        }
        self._conn = mysql.connector.connect(**config)
        self._cursor = self._conn.cursor()
        
    # https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cursor.close()
        self._conn.close()

    def player_results(self, player: str) -> Result:
        # Returns the summarised results for a player

        # Get overall stats
        player_sql = """SELECT
                    SUM(kills) AS kills,
                    SUM(deaths) AS deaths,
                    SUM(assists) AS assists,
                    MAX(biggest_kill_streak) AS biggest_kill_streak,
                    COUNT(1) AS matches,
                    SUM(won) AS wins,
                    AVG(gpm) AS gpm,
                    AVG(xpm) AS xpm,
                FROM player_matches
                WHERE player = %s
                GROUP BY player
            """
        results = self._cursor.execute(player_sql, (player)).fetchall()
        for result in results:
            #only expecting one row
            kills = result[0]
            deaths = result[1]
            assists = result[2]
            kill_streak = result[3]
            matches = result[4]
            wins = result[5]
            gpm = result[6]
            xpm = result[7]

        # Get top heroes
        hero_sql = """SELECT
                    hero,
                    COUNT(1) AS matches,
                    SUM(won) AS wins,
                    AVG(kills) AS kills,
                    AVG(deaths) AS deaths,
                    AVG(assists) AS assists,
                    AVG(gpm) AS gpm,
                    AVG(xpm) AS xpm,
                    MAX(biggest_kill_streak) AS biggest_kill_streak
                FROM player_matches
                WHERE player = %s
                GROUP BY player, hero
                ORDER BY 2 DESC
                """
        results = self._cursor.execute(hero_sql, (player)).fetchall()
        heroes = []
        for result in results:
            heroes.append(
                {
                    "name": result[0],
                    "matches": result[1],
                    "wins": result[2],
                    "kills": result[3],
                    "deaths": result[4],
                    "assists": result[5],
                    "gpm": result[6],
                    "xpm": result[7],
                    "kill_streak": result[8]
                }
            )

        return {
            "player": player,
            "matches": matches,
            "wins": wins,
            "kills": kills,
            "deaths": deaths,
            "assists": assists,
            "kill_streak": kill_streak,
            "heroes": heroes
        }

    def match_results(self, match_id: int) -> Result:
        # Returns the result for a match

        # Match summary
        match_sql = """
                    SELECT
                        radiant_team,
                        dire_team,
                        winner,
                        radiant_kills,
                        dire_kills,
                        duration
                    FROM matches
                    WHERE match_id = %s
                    """

        for result in self._cursor.execute(match_sql, (match_id)):
            radiant_team = result[0]
            dire_team = result[1]
            winner = result[2]
            radiant_kills = result[3]
            dire_kills = result[4]
            duration = result[5]

        # Hero summary
        match_heroes_sql = """
                    SELECT
                        hero,
                        side,
                        player,
                        kills,
                        deaths,
                        assists,
                        gpm,
                        xpm
                    FROM player_matches
                    WHERE match_id = %s
                    """

        heroes = {
            "radiant": [],
            "dire": []
        }
        for result in self._conn.execute(match_heroes_sql, (match_id)):
            if result[1] = "Radiant":
                heroes['radiant'].append(
                    {
                        "hero": result[0],
                        "player": result[2],
                        "kills": result[3],
                        "deaths": result[4],
                        "assists": result[5],
                        "gpm": result[6],
                        "xpm": results[7]
                    }
                )
            else:
                heroes['dire'].append(
                    {
                        "hero": result[0],
                        "player": result[2],
                        "kills": result[3],
                        "deaths": result[4],
                        "assists": result[5],
                        "gpm": result[6],
                        "xpm": results[7]
                    }
                )

        return {
            "radiant_team": radiant_team,
            "dire_team": dire_team,
            "winner": winner,
            "radiant_kills": radiant_kills,
            "dire_kills": dire_kills,
            "duration": duration,
            "heroes": heroes
        }

    def team_results(self, team: str) -> Result:
        # Returns the summarised results for the chosen team
        return {
            "name": "Lost Mid, Again",
            "wins": 5,
            "losses": 3,
            "radiant_wins": 4,
            "radiant_losses": 0,
            "dire_wins": 1,
            "dire_losses": 3,
            "matches": [
                {
                    "against": "AWOOGA",
                    "result": "won",
                    "match_id": 12345
                },
                {
                    "against": "Sorry for your captain",
                    "result": "lost",
                    "match_id": 23456
                }
            ],
            "picks": [
                {
                    "name": "Pudge",
                    "picks": 8,
                    "wins": 2,
                    "winrate": "25%"
                },
                {
                    "name": "Sven",
                    "picks": 5,
                    "wins": 4,
                    "winrate": "80%"
                }
            ],
            "bans": [
                {
                    "name": "Riki",
                    "bans": 4,
                    "wins_against": 1,
                    "losses_against": 3
                },
                {
                    "name": "Techies",
                    "bans": 9,
                    "wins_against": 0,
                    "losses_against": 1
                }
            ]
        }