from api.screen_clear import screen_clear

def data_save_option() -> int:
    """Approval function for saving data in table
    * return 1 - Yes
    * return 0 - No
    * return -1 - Error: Inccorect input
    """

    option = input('Do you confirm that entered data is correct? [Y, y | N, n]: ')
    if option in ('Y', 'y'):
        screen_clear()
        return 1
    elif option in ('N', 'n'):
        screen_clear()
        return 0
    else:
        print('Error: The entered data does not correspond to the available letters (Y, N, y, n). Please repeat the input again...')
        input('Press enter to continue...')
        screen_clear()
        return -1
