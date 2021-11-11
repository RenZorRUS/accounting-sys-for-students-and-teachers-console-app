from os import path
from api.main_menu import main_menu
from api.check_db import check_db
from api.screen_clear import screen_clear

BASE_DIR = path.dirname(path.abspath(__file__))
db_path = path.join(BASE_DIR, 'db.sqlite3')

check_db(db_path)
main_menu(db_path)
screen_clear()