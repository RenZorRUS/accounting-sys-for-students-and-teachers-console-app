from sqlite3 import OperationalError, IntegrityError
from api.screen_clear import screen_clear
from api.view_list import view_subjects_list
from .modules.data_save_option import data_save_option
from .modules.curr_table_message import curr_table_message
import re

class Subject():
    def __init__(self):
        self.subject_name = None

    def add_row(self, db_cursor) -> None:
        """Add row to the table"""

        # Subject name
        while True:
            curr_table_message('Subject')
            view_subjects_list(db_cursor)
            self.subject_name = input('Enter subject_name: ')
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
                f"""INSERT INTO subjects(subject_name)
                    VALUES( "{self.subject_name}" )
                """
            )
            print('\nData saved...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not saved to the table, possible reasons:

                   * Subject name must be unique
                """
            )

    def delete_row(self, db_cursor) -> None:
        """Delete row from the table"""
        subject_id = 0

        # Subject ID
        while True:
            view_subjects_list(db_cursor)
            try:
                subject_id = int(input('Enter subject id number: '))
            except ValueError:
                print('Error: enter subject id (number > or = 1) again...')
                continue
            else:
                if 1 <= subject_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter subject id (number > or = 1) again...')
                continue

        try:
            db_cursor.execute(
                f"""DELETE FROM subjects WHERE subject_id = {subject_id}
                """
            )
            print('\nData deleted...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not deleted from the table, possible reasons:

                    * The subject with the entered subject ID doesn't exist
                    * The subject table is empty
                """
            )

    def edit_row(self, db_cursor) -> None:
        """Edit row in the table"""

        # Identification of data in need of change by adding variable names
        # Data in the list must match the names of fields in the table
        changing_data = []
        subject_id = 0

        # Subject ID
        while True:
            screen_clear()
            view_subjects_list(db_cursor)
            try:
                subject_id = int(input('Enter subject id number: '))
            except ValueError:
                print('Error: enter subject id (number > or = 1) again...')
                continue
            else:
                if 1 <= subject_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter subject id (number > or = 1) again...')
                input('Press enter to continue...')
                continue

        # Editing row by selected ID
        # Subject name
        while True:
            screen_clear()
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

                if 'subject_name' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        subject_name = "{self.subject_name}"
                        """
                    )

                db_cursor.execute(
                    f"""UPDATE subjects
                        SET {','.join(sets_in_sql_query)}
                        WHERE subject_id = {subject_id}
                    """
                )
                print('\nData edited...\n')
            else:
                print('\nData not edited...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not edited in the table, possible reasons:

                    * The subject with the entered subject ID doesn't exist
                    * The subject table is empty
                    * Subject name must be unique
                """
            )
