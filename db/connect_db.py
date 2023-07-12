import mysql.connector


class mydb:
    def __init__(self) -> None:
        self.db = 0


    def open_connect(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="GTai",
            password="DS18099081MySqlDB1331",
            database="discord"
        )


    def open_connect_courses(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="GTai",
            password="DS18099081MySqlDB1331",
            database="courses"
        )


    def close_connect(self):
        self.db.close()