from sqlite3 import OperationalError, IntegrityError
from api.screen_clear import screen_clear
from api.view_list import view_teachers_list, view_subjects_list
from .modules.data_save_option import data_save_option
from .modules.curr_table_message import curr_table_message
import re

class Teacher():
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.subject_name = None

    def add_row(self, db_cursor) -> None:
        """Add row to the table"""

        # First name
        while True:
            curr_table_message('Teacher')
            view_teachers_list(db_cursor)
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
            curr_table_message('Teacher')
            view_teachers_list(db_cursor)
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
            curr_table_message('Teacher')
            view_teachers_list(db_cursor)
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

        # Subject name
        while True:
            curr_table_message('Teacher')
            view_subjects_list(db_cursor)
            self.subject_name = input('Enter subject name: ')
            if re.match(r'^([А-Я]{1}[а-яё ]{1,98}|[A-Z]{1}[a-z ]{1,98})$', self.subject_name):
                option = data_save_option()
                if option == 1:
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter subject name (no more than 100 characters) again...')

        try:
            db_cursor.execute(
                f"""INSERT INTO teachers(first_name, last_name, email, subject_id)
                    VALUES( "{self.first_name}", "{self.last_name}", "{self.email}", 
                            (SELECT subject_id FROM subjects WHERE subject_name = "{self.subject_name}") )
                """
            )
            print('\nData saved...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not saved to the table, possible reasons:

                    * The teacher's email matches the email of another teacher (email must be unique)
                    * There is no subject with the entered name in Subjects table
                """
            )

    def delete_row(self, db_cursor) -> None:
        """Delete row from the table"""
        teacher_id = 0

        # Teacher ID
        while True:
            view_teachers_list(db_cursor)
            try:
                teacher_id = int(input('Enter teacher id number: '))
            except ValueError:
                print('Error: enter teacher id (number > or = 1) again...')
                continue
            else:
                if 1 <= teacher_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter teacher id (number > or = 1) again...')
                continue

        try:
            db_cursor.execute(
                f"""DELETE FROM teachers WHERE teacher_id = {teacher_id}
                """
            )
            print('\nData deleted...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not deleted from the table, possible reasons:

                    * The teacher with the entered teacher ID doesn't exist
                    * The teachers table is empty
                """
            )

    def edit_row(self, db_cursor) -> None:
        """Edit row in the table"""

        # Identification of data in need of change by adding variable names
        # Data in the list must match the names of fields in the table
        changing_data = []
        teacher_id = 0

        # Teacher id
        while True:
            screen_clear()
            view_teachers_list(db_cursor)
            try:
                teacher_id = int(input('Enter teacher id number: '))
            except ValueError:
                print('Error: enter teacher id (number > or = 1) again...')
                continue
            else:
                if 1 <= teacher_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter teacher id (number > or = 1) again...')
                input('Press enter to continue...')
                continue

        # Editing row by selected ID
        # First name
        while True:
            screen_clear()
            view_teachers_list(db_cursor)
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
            view_teachers_list(db_cursor)
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
            view_teachers_list(db_cursor)
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

        # Subject name
        while True:
            screen_clear()
            view_teachers_list(db_cursor)
            view_subjects_list(db_cursor)
            self.subject_name = input(
                "Enter subject name (or press enter if you don't want to change the data): ")
            if self.subject_name == '':
                break
            if re.match(r'^([А-Я]{1}[а-яё ]{1,98}|[A-Z]{1}[a-z ]{1,98})$', self.subject_name):
                option = data_save_option()
                if option == 1:
                    changing_data.append('subject_name')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter subject name (no more than 100 characters) again...')

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

                if 'subject_name' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        subject_id = (
                            SELECT subject_id
                            FROM subjects
                            WHERE subject_name = "{self.subject_name}"
                        )
                        """
                    )

                db_cursor.execute(
                    f"""UPDATE teachers
                        SET {','.join(sets_in_sql_query)}
                        WHERE teacher_id = {teacher_id}
                    """
                )
                print('\nData edited...\n')
            else:
                print('\nData not edited...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not edited in the table, possible reasons:

                    * The teacher with the entered teacher ID doesn't exist
                    * The teachers table is empty
                    * The subject with entered name doesn't exist or the subject table is empty
                """
            )
