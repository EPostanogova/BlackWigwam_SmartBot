import sqlite3
from sqlite3 import Error

import logging

logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filemode='w',
        )


class Database:
    def __init__(self,db_path):

        self.logger = logging.getLogger('BD')
        self.db_path=db_path
        try:
            self.con = sqlite3.connect(self.db_path)
            self.cursorObj = self.con.cursor()
            self.logger.info("Connection to SQLite DB successful")
        except Error:
            self.logger.error("The error occurred")

    def create_users_table(self):

        try:
            self.cursorObj.execute(
                "CREATE TABLE IF NOT EXISTS Users(id integer PRIMARY KEY, user_id integer NOT NULL, first_name text NOT NULL , last_name text)")
            self.con.commit()
            self.logger.info("table created")
        except Error:
            self.logger.error("No table created")

    def add_new_user(self, user_info):
        key = 'id' in user_info
        if key==False:
            raise KeyError ('Не найден ключ id')
            INSERT IGNORE INTO TABLE( )

            self.cursorObj.execute('INSERT INTO Users(id,  user_id, first_name, last_name) VALUES(?, ?, ?, ?)''', user_info)



