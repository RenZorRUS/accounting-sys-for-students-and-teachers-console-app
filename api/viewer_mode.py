from .view_list import view_list
from .screen_clear import screen_clear

def viewer_mode(db_path) -> bool:
    """This mode allows you to:
        * View students, teachers or groups list
        * View subjects or assessments list"""
    option = 0

    screen_clear()
    print(
        """Current mode: Viewer
        
        This mode allows you to:
        * View students, teachers or groups list
        * View subjects or assessments list

        Please select next action:
        1) - View students list
        2) - View teachers list
        3) - Viewing groups list
        4) - View subjects list
        5) - View assessments list
        6) - Changing the mode
        7) - Exit
        """
    )

    while True:
        try:
            option = int(input('Enter the number of option: '))
        except ValueError:
            print('Error: please enter an available option from (1 - 7)...')
            continue
        else:
            if option in (1, 2, 3, 4, 5):
                view_list(option, db_path)
                input('Press enter to continue...')

                # end_of_program = False, change_mode = False
                return(False, False)
            elif option == 6:
                # end_of_program = False, change_mode = True
                return (False, True)
            elif option == 7:
                # end_of_program = True, change_mode = True
                return (True, True)
            print('Error: please enter an available option from (1 - 7)...')
            continue
