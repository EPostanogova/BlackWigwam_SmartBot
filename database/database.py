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
        x=user_info['user_id']
        y=user_info['first_name']
        z=user_info['last_name']

        if 'id' not in user_info:
            raise KeyError ('Not key found')
        try:
            self.cursorObj.execute('INSERT OR IGNORE INTO Users(user_id, first_name, last_name) VALUES(?,?,?)',(x,y,z))
            self.con.commit()
            self.logger.info('User added')
        except Error as r:
            self.logger.error('User not added',r)

    def get_all_records(self,table_name):
        try:
            self.cursorObj.execute('SELECT  * FROM 'f'{table_name}''')
            all_results= self.cursorObj.fetchall()
            print(all_results)
        except Error:
            self.logger.error('err')

    def drop_table(self,table_name):
        try:
            self.cursorObj.execute('DROP table if exists 'f'{table_name}''')
            self.logger.info('Removed')
        except Error:
            self.logger.error('Not Removed')

    def create_commands_table(self):
        try:
            self.cursorObj.execute(
                "CREATE TABLE IF NOT EXISTS Cmd_table(id integer PRIMARY KEY, command text NOT NULL, user_id integer , time_stamp TIMESTAMP)")
            self.con.commit()
            self.logger.info("cmd-table created")

        except Error:
            self.logger.error("No cmd-table created")

    def add_command(self,info):
        x = info['command']
        y = info['user_id']
        z = info['time_stamp']

        try:
            self.cursorObj.execute('INSERT OR IGNORE INTO Cmd_table(command, user_id, time_stamp) VALUES(?,?,?)',
                                   (x, y, z))
            self.con.commit()
            self.logger.info('Command added')
        except Error as e:
            self.logger.error('Command not added',e)



