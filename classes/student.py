from sqlite3 import OperationalError, IntegrityError
from api.view_list import view_students_list
from api.screen_clear import screen_clear
from .modules.data_save_option import data_save_option
from .modules.curr_table_message import curr_table_message
import re

class Student():
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.date_of_birth = None
        self.course = None
        self.group_num = None

    def add_row(self, db_cursor) -> None:
        """Add row to the table"""

        # First name
        while True:
            curr_table_message('Student')
            view_students_list(db_cursor)
            self.first_name = input('Enter first name: ')
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.first_name):
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    """Error: Inccorect input, please enter the data according to rules:
                    
                    * The first letter should be (A - Z) or (А - Я)
                    * The following letters should be (a - z) or (а - я)
                    * The string must be no more than 25 characters
                    """
                )

        # Last name
        while True:
            curr_table_message('Student')
            view_students_list(db_cursor)
            self.last_name = input('Enter last name: ')
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.last_name):
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    """Error: Inccorect input, please enter the data according to rules:
                    
                    * The first letter should be (A - Z) or (А - Я)
                    * The following letters should be (a - z) or (а - я)
                    * The string must be no more than 25 characters
                    """
                )

        # Email
        while True:
            curr_table_message('Student')
            view_students_list(db_cursor)
            self.email = input('Enter email: ')
            if re.match(r"""(?:[a-z0-9!#$%&'*+ /=?^_`{ | }~-]+(?: \.[a-z0-9!  # $%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
                        self.email):
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter email (no more than 70 characters) again...')

        # Date of birth
        while True:
            curr_table_message('Student')
            view_students_list(db_cursor)
            self.date_of_birth = input(
                'Enter date of birth in format YYYY-MM-DD: ')
            if re.match(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$', self.date_of_birth):
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter date of birth in format YYYY-MM-DD again...')

        # Course
        while True:
            curr_table_message('Student')
            view_students_list(db_cursor)
            self.course = int(input('Enter course number: '))
            if 1 <= self.course <= 5:
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter course number (1 - 5) again...')

        # Group number
        while True:
            curr_table_message('Student')
            view_students_list(db_cursor)
            self.group_num = input('Enter group number: ')
            if re.match(r'^\d{1,10}$', self.group_num):
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter group number (no more than 10 characters) again...')

        try:
            db_cursor.execute(
                f"""INSERT INTO students(first_name, last_name, email, date_of_birth, course, group_id)
                    VALUES( "{self.first_name}", "{self.last_name}", "{self.email}", "{self.date_of_birth}",
                            "{self.course}", (SELECT group_id FROM groups_table WHERE group_num = "{self.group_num}") )
                """
            )
            print('\nData saved...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not saved to the table, possible reasons:

                    * The student's email matches the email of another student (email must be unique)
                    * There is no group with the entered number in Groups table
                """
            )

    def delete_row(self, db_cursor) -> None:
        """Delete row from the table"""
        student_id = 0

        screen_clear()

        # Student ID
        while True:
            view_students_list(db_cursor)
            try:
                student_id = int(input('Enter student id number: '))
            except ValueError:
                print('Error: enter student id (number > or = 1) again...')
                continue
            else:
                if 1 <= student_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter student id (number > or = 1) again...')
                continue

        try:
            db_cursor.execute(
                f"""DELETE FROM students WHERE student_id = {student_id}
                """
            )
            print('\nData deleted...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not deleted from the table, possible reasons:

                    * The student with the entered student ID doesn't exist
                    * The student table is empty
                """
            )

    def edit_row(self, db_cursor) -> None:
        """Edit row in the table"""

        # Identification of data in need of change by adding variable names
        # Data in the list must match the names of fields in the table
        changing_data = []
        student_id = 0

        screen_clear()

        # Student ID
        while True:
            screen_clear()
            view_students_list(db_cursor)
            try:
                student_id = int(
                    input('Enter student ID number you want to change: '))
            except ValueError:
                print('Error: enter student id (number > or = 1) again...')
                continue
            else:
                if 1 <= student_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter student id (number > or = 1) again...')
                input('Press enter to continue...')
                continue

        # Editing row by selected ID
        # First name
        while True:
            screen_clear()
            view_students_list(db_cursor)
            self.first_name = input(
                "Enter first name (or press enter if you don't want to change the data): ")
            if self.first_name == '':
                break
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.first_name):
                option = data_save_option()
                if option == 1:
                    changing_data.append('first_name')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    """Error: Inccorect input, please enter the data according to rules:
                    
                    * The first letter should be (A - Z) or (А - Я)
                    * The following letters should be (a - z) or (а - я)
                    * The string must be no more than 25 characters
                    """
                )

        # Last name
        while True:
            screen_clear()
            view_students_list(db_cursor)
            self.last_name = input(
                "Enter last name (or press enter if you don't want to change the data): ")
            if self.last_name == '':
                break
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.last_name):
                option = data_save_option()
                if option == 1:
                    changing_data.append('last_name')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    """Error: Inccorect input, please enter the data according to rules:
                    
                    * The first letter should be (A - Z) or (А - Я)
                    * The following letters should be (a - z) or (а - я)
                    * The string must be no more than 25 characters
                    """
                )

        # Email
        while True:
            screen_clear()
            view_students_list(db_cursor)
            self.email = input(
                "Enter email (or press enter if you don't want to change the data): ")
            if self.email == '':
                break
            if re.match(r"""(?:[a-z0-9!#$%&'*+ /=?^_`{ | }~-]+(?: \.[a-z0-9!  # $%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
                        self.email):
                option = data_save_option()
                if option == 1:
                    changing_data.append('email')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter email (no more than 70 characters) again...')

        # Date of birth
        while True:
            screen_clear()
            view_students_list(db_cursor)
            self.date_of_birth = input(
                "Enter date of birth in format YYYY-MM-DD (or press enter if you don't want to change the data): ")
            if self.date_of_birth == '':
                break
            if re.match(r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$', self.date_of_birth):
                option = data_save_option()
                if option == 1:
                    changing_data.append('date_of_birth')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter date of birth in format YYYY-MM-DD again...')

        # Course
        while True:
            screen_clear()
            view_students_list(db_cursor)
            self.course = input(
                "Enter course number (or press enter if you don't want to change the data): ")
            if self.course == '':
                break
            if re.match(r'^\d{1}$', self.course):
                option = data_save_option()
                if option == 1:
                    changing_data.append('course')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter course (no more than 1 digit) number again...')

        # Group number
        while True:
            screen_clear()
            view_students_list(db_cursor)
            self.group_num = input(
                "Enter group number (or press enter if you don't want to change the data): ")
            if self.group_num == '':
                break
            if re.match(r'^\d{10}$', self.group_num):
                option = data_save_option()
                if option == 1:
                    changing_data.append('group_num')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print('Error: Inccorect input, please enter group number (no more than 10 characters) again...')

        try:
            if len(changing_data) != 0:
                sets_in_sql_query = []

                if 'first_name' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        first_name = "{self.first_name}"
                        """
                    )

                if 'last_name' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        last_name = "{self.last_name}"
                        """
                    )

                if 'email' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        email = "{self.email}"
                        """
                    )

                if 'date_of_birth' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        date_of_birth = "{self.date_of_birth}"
                        """
                    )

                if 'course' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        course = {self.course}
                        """
                    )

                if 'group_num' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        group_id = (
                            SELECT group_id
                            FROM groups_table
                            WHERE group_num = "{self.group_num}"
                        )
                        """
                    )

                db_cursor.execute(
                    f"""UPDATE students
                        SET {','.join(sets_in_sql_query)}
                        WHERE student_id = {student_id}
                    """
                )
                print('\nData edited...\n')
            else:
                print('\nData not edited...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not edited in the table, possible reasons:

                    * The student's email matches the email of another student (email must be unique)
                    * There is no group with the entered number in Groups table
                """
            )
