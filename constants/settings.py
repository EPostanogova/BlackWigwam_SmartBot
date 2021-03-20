import os 

from os.path import join 

ROOT_DIR = os.path.abspath(join("bot.py", '..', '..'))
DATA_DIR = join(ROOT_DIR, 'aiogram_bot", "data')
DB_DATA = join(ROOT_DIR, 'aiogram_bot/database/data/data.db')