from replay_summary import ReplaySummariser
import mysql.connector

class DbClient():

    def __init__(self, rs: ReplaySummariser) -> None:
        self.rs = rs

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'ascendant'
        }
        self._conn = mysql.connector.connect(**config)
        self._cursor = self._conn.cursor()

    # https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._cursor.close()
        self._conn.close()

    def insert(self) -> None:
        # Inserts the parsed data into the DB
        raise NotImplementedError
