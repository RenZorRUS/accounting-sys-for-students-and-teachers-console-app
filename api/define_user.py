def define_user() -> int:
    """ Defining a user:
    * Viewer mode - returns 1
    * Admin mode - returns 2
    * Exit - returns 3"""
    option = 0

    print(
        """
        Please, specify operating mode or action:
        1) - Viewer
        2) - Admin
        3) - Exit
        """
    )
    while True:
        try:
            option = int(input('Enter the number of option: '))
        except ValueError:
            print(
                'Error: enter the available number of options (1 - 3)...')
            continue
        else:
            if option in (1, 2):
                break
            elif option == 3:
                break
            print('Error: enter the available number of options (1 - 3)...')
            continue

    return option