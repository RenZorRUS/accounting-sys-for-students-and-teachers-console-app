from .define_user import define_user
from .viewer_mode import viewer_mode
from .admin_mode import admin_mode

def main_menu(db_path) -> None:
    """ Console menu """

    end_of_program = False
    change_mode = False
    print('\n<--- Accounting system for Students and Teachers --->')
    while not end_of_program:
        change_mode = False
        if define_user() == 1:
            while not change_mode:
                end_of_program, change_mode = viewer_mode(db_path)
        else:
            while not change_mode:
                end_of_program, change_mode = admin_mode(db_path)
