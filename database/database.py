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
            con = sqlite3.connect(self.db_path)
            self.logger.info("Connection to SQLite DB successful")
        except Error:
            self.logger.error("The error occurred")

