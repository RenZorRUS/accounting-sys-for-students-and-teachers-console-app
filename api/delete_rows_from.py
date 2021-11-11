from .screen_clear import screen_clear
from classes.assessments import Assessment
from classes.group import Group
from classes.student import Student
from classes.teacher import Teacher
from classes.subject import Subject


def delete_rows_from(db_cursor) -> None:
    """Delete rows from selected table"""

    screen_clear()

    print(
        """From which table do you want to delete data?

        1) - Students
        2) - Teachers
        3) - Groups
        4) - Subjects
        5) - Assessments
        6) - Back
        """
    )

    while True:
        try:
            option = int(input('Enter the number of option: '))
        except ValueError:
            print('Error: please enter an available option from (1 - 6)...')
            continue
        else:
            if option in (1, 2, 3, 4, 5):
                options = {
                    1: Student,
                    2: Teacher,
                    3: Group,
                    4: Subject,
                    5: Assessment
                }

                # Object with selected type
                obj = options[option]()
                while True:
                    obj.delete_row(db_cursor)
                    option = input('Continue deleting data? [Y, y | N, n]: ')
                    if option in ('Y', 'y'):
                        continue
                    elif option in ('N', 'n'):
                        break
                    else:
                        print(
                            'Error: The entered data does not correspond to the available letters (Y, N, y, n)...')
                        input('Press enter to continue...')
                    break

                break

            elif option == 6:
                break

            print('Error: please enter an available option from (1 - 6)...')
            continue
