from os import name, system

def screen_clear():
    """Clears the console screen by command dependent on os.name (Windows, Mac, Linux)"""

    # For MAC and Linux(os.name is 'POSIX')
    if name == 'posix':
        system('clear')
    else:
        # For windows
        system('cls')
