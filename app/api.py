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
                    "wins": 2
                },
                {
                    "name": "Sven",
                    "picks": 5,
                    "wins": 4
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