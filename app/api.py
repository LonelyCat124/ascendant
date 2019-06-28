import mysql.connector

class ApiClient():
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': '3306',
            'database': 'ascendant'
        }
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        
    # https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
    def __enter__(self):
        return self

    def __exit(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()