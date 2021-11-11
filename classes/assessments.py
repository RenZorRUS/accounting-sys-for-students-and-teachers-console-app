from sqlite3 import OperationalError, IntegrityError
from api.screen_clear import screen_clear
from api.view_list import view_assessments_list, view_students_list, view_subjects_list
from .modules.data_save_option import data_save_option
from .modules.curr_table_message import curr_table_message
import re

class Assessment():
    def __init__(self):
        self.students_first_name = None
        self.students_last_name = None
        self.assessment = None
        self.subject_name = None

    def add_row(self, db_cursor) -> None:
        """Add row to the table"""

        # Students first name
        while True:
            curr_table_message('Assessment')
            view_students_list(db_cursor)
            self.students_first_name = input(
                "Enter student's first name name: ")
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.students_first_name):
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

        # Students last name
        while True:
            curr_table_message('Assessment')
            view_students_list(db_cursor)
            self.students_last_name = input("Enter student's last name: ")
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.students_last_name):
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

        # Assessment
        while True:
            curr_table_message('Assessment')
            try:
                self.assessment = int(input('Enter assessment: '))
            except ValueError:
                print('Error: enter assessment (number from 0 to 10) again...')
                continue
            else:
                if 0 <= self.assessment <= 10:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter assessment (number from 0 to 10) again...')
                continue

        # Subject name
        while True:
            curr_table_message('Assessment')
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
                f"""INSERT INTO subject_assessments(assessment, student_id, subject_id)
                    VALUES( {self.assessment},
                            (SELECT student_id FROM students WHERE first_name = "{self.students_first_name}" AND last_name = "{self.students_last_name}"),
                            (SELECT subject_id FROM subjects WHERE subject_name = "{self.subject_name}") )
                """
            )
            print('\nData saved...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not saved to the table, possible reasons:

                    * The student with the entered first and last name doesn't exist
                    * There is no subject with the entered name in Subjects table
                """
            )

    def delete_row(self, db_cursor) -> None:
        """Delete row from the table"""
        assessment_id = 0

        screen_clear()

        # Assessment ID
        while True:
            view_assessments_list(db_cursor)
            try:
                assessment_id = int(input('Enter assessment id number: '))
            except ValueError:
                print('Error: enter assessment id (number > or = 1) again...')
                continue
            else:
                if 1 <= assessment_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter assessment id (number > or = 1) again...')
                continue

        try:
            db_cursor.execute(
                f"""DELETE FROM subject_assessments WHERE assessment_id = {assessment_id}
                """
            )
            print('\nData deleted...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not deleted from the table, possible reasons:

                    * The assessment with the entered assessment ID doesn't exist
                    * The subject_assessments table is empty
                """
            )

    def edit_row(self, db_cursor) -> None:
        """Edit row in the table"""

        # Identification of data in need of change by adding variable names
        # Data in the list must match the names of fields in the table
        changing_data = []
        assessment_id = 0

        # Assessment ID
        while True:
            screen_clear()
            view_assessments_list(db_cursor)
            try:
                assessment_id = int(input('Enter assessment id number: '))
            except ValueError:
                print('Error: enter assessment id (number > or = 1) again...')
                continue
            else:
                if 1 <= assessment_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter assessment id (number > or = 1) again...')
                input('Press enter to continue...')
                continue

        # Editing row by selected ID
        # Students first name
        while True:
            screen_clear()
            view_assessments_list(db_cursor)
            input_str = ''.join([
                "To change the student's data in the assessments table,\n",
                "You need to enter it first_name and last_name(1 of the parameters cannot be empty).\n",
                "If you don't need to change them, just press enter on them.\n\n",
                "Enter student's first name (or press enter if you don't want to change the data): "
            ])
            self.students_first_name = input(input_str)
            if self.students_first_name == '':
                break
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.students_first_name):
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

        # Students last name
        while True:
            screen_clear()
            view_assessments_list(db_cursor)
            self.students_last_name = input(
                "Enter student's last name (or press enter if you don't want to change the data): ")
            if self.students_last_name == '':
                break
            if re.match(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$', self.students_last_name):
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

        # Assessment
        while True:
            screen_clear()
            view_assessments_list(db_cursor)
            try:
                self.assessment = (input(
                    "Enter assessment (or press enter if you don't want to change the data): "))
                if self.assessment == '':
                    break
                else:
                    # Conversion after testing on ''
                    self.assessment = int(self.assessment)
            except ValueError:
                print('Error: enter assessment (number from 0 to 10) again...')
                continue
            else:
                if 0 <= self.assessment <= 10:
                    option = data_save_option()
                    if option == 1:
                        changing_data.append('assessment')
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter assessment (number from 0 to 10) again...')
                continue

        # Subject name
        while True:
            screen_clear()
            view_subjects_list(db_cursor)
            self.subject_name = input("Enter email (or press enter if you don't want to change the data): ")
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

                if 'first_name' and 'last_name' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        subject_assessments.student_id = (
                                SELECT student_id 
                                FROM students 
                                WHERE first_name = "{self.students_first_name}"
                                  AND last_name = "{self.students_last_name}"
                            )
                        """
                    )

                if 'assessment' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        assessment = {self.assessment}
                        """
                    )

                if 'subject_name' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        subject_assessments.subject_id = (
                                SELECT subject_id
                                FROM subjects
                                WHERE subject_name = "{self.subject_name}"
                            )
                        """
                    )

                db_cursor.execute(
                    f"""UPDATE subject_assessments
                        SET {','.join(sets_in_sql_query)}
                        WHERE assessment_id = {assessment_id}
                    """
                )
                print('\nData edited...\n')
            else:
                print('\nData not edited...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not edited in the table, possible reasons:

                    * The assessment with the entered assessment ID doesn't exist
                    * 1 of parameters student's first or last name is empty
                    * The subject_assessments or students table is empty
                """
            )
