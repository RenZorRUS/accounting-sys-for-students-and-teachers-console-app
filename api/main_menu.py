from .define_user import define_user
from .viewer_mode import viewer_mode
from .admin_mode import admin_mode
from .screen_clear import screen_clear

def main_menu(db_path) -> None:
    """ Console menu """
    end_of_program = False
    
    while not end_of_program:
        screen_clear()
        print('<--- Accounting system for Students and Teachers --->')
        option = define_user()
        change_mode = False
        if option == 1:
            while not change_mode:
                end_of_program, change_mode = viewer_mode(db_path)
        elif option == 2:
            while not change_mode:
                end_of_program, change_mode = admin_mode(db_path)
        else:
            return
