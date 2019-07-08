from replay_summary import ReplaySummariser
import mysql.connector

class DbClient():

    def __init__(self, rs: ReplaySummariser) -> None:
        """
        Takes a summarised replay `ReplaySummariser` and inserts the results into the DB
        :param rs: ReplaySummariser A summarised match replay
        """
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

    def insert_match(self) -> None:
        """
        Inserts the match summary into the DB
        :return: None
        """

        raise NotImplementedError

    def insert_players(self) -> None:
        """
        Inserts the player summaries into the DB
        :return: None
        """
        raise NotImplementedError
