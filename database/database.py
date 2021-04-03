import sqlite3
from sqlite3 import Error

import logging

logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s : %(levelname)s : %(message)s',
            filemode='w',
        )

import os
from os.path import join


from constants.settings import DB_DATA


class Database:
    def __init__(self):
        db_path = DB_DATA
        self.logger = logging.getLogger('BD')
        try:
            con = sqlite3.connect(db_path)
            self.logger.info("Connection to SQLite DB successful")
        except Error as e:
            self.logger.error("The error '{e}' occurred")

