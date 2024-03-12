import mysql.connector
from mysql.connector import errorcode

config = {"user": "root", "password": "password", "database": "db_tbi"}


class DatabaseConnection:
    def __init__(self):
        try:
            self.db_connect = mysql.connector.connect(**config)
            self.cursor = self.db_connect.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def select(self, query):
        self.cursor.execute(query)
        self.data = self.cursor.fetchall()
        return self.data

    def close_connection(self):
        self.cursor.close()
        self.db_connect.close()