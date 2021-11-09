from .view_list import view_list

def viewer_mode(db_path) -> bool:
    """This mode allows you to:
        * View lists of students, teachers and groups
        * View list of groups"""
    option = 0

    print(
        """Current mode: Viewer
        
        This mode allows you to:
        * View student, teacher and group lists
        * View subject list

        Please select next action:
        1) - View student lists
        2) - View teacher lists
        3) - Viewing lists of groups
        4) - View the list of available academic subjects
        5) - Changing the mode
        6) - Exit
        """
    )

    while True:
        try:
            option = int(input('Please, enter the number of option: '))
        except ValueError:
            print('Error: please enter an available option from (1, 2, 3, 4, 5, 6)...')
            continue
        else:
            if option in (1, 2, 3, 4):
                view_list(option, db_path)
                break
            elif option == 5:
                # end_of_program = False, change_mode = True
                return (False, True)
            elif option == 6:
                # end_of_program = True, change_mode = True
                return (True, True)
            print('Error: please enter an available option from (1, 2, 3, 4, 5, 6)...')
            continue