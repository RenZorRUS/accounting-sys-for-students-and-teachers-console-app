import sqlite3

from api.screen_clear import screen_clear
from .view_list import view_list
from .add_rows_to import add_rows_to
from .delete_rows_from import delete_rows_from
from .edit_rows_in import edit_rows_in


def admin_mode(db_path):
    """This mode allows you to:
        * View students, teachers or groups list
        * View subjects or assessments list
        * Adding new rows to the tables
        * Delete rows from the tables
        * Edit rows in the tables"""

    print(
        """Current mode: Admin
        
        This mode allows you to:
        * View students, teachers or groups list
        * View subjects or assessments list
        * Adding new rows to the tables
        * Delete rows from the tables
        * Edit rows in the tables

        Please select the next action:
        1) - View students list 
        2) - View teachers list 
        3) - View groups list
        4) - View academic subjects list
        5) - View assessments list
        6) - Add new rows to ...
        7) - Delete rows from ...
        8) - Edit rows in ...
        9) - Changing the mode
        10) - Exit
        """
    )

    while True:
        try:
            option = int(input('Enter the number of option: '))
        except ValueError:
            print('Error: enter the available number of options (1 - 10)...')
            continue
        else:
            if option in (1, 2, 3, 4, 5):
                view_list(option, db_path)
                input('Press enter to continue...')

                # end_of_program = False, change_mode = False
                return(False, False)
            elif option in (6, 7, 8):
                options = {
                    6: add_rows_to,
                    7: delete_rows_from,
                    8: edit_rows_in
                }
                db_connect = sqlite3.connect(db_path)
                db_cursor = db_connect.cursor()

                selected_func = options[option]
                selected_func(db_cursor)

                db_connect.commit()
                db_connect.close()

                # end_of_program = False, change_mode = False
                return (False, False)
            elif option == 9:
                # end_of_program = False, change_mode = True
                return (False, True)
            elif option == 10:
                # end_of_program = True, change_mode = True
                return (True, True)
            print('Error: enter the available number of options (1 - 10)...')
            continue
