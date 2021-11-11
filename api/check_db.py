from os import path
from .create_db import create_db

def check_db(db_path) -> None:
    """Checks if the database exists in the program directory, if not, creates a new one"""

    if path.isfile(db_path):
        return
    else:
        db_file = open(db_path, 'w')
        db_file.close()
        create_db(db_path)
        return
