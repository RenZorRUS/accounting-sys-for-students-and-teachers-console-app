from sqlite3 import OperationalError, IntegrityError
from api.screen_clear import screen_clear
from api.view_list import view_groups_list
from .modules.data_save_option import data_save_option
from .modules.curr_table_message import curr_table_message
import re

class Group():
    def __init__(self):
        self.group_num = None
        self.group_email = None

    def add_row(self, db_cursor) -> None:
        """Add row to the table"""

        # Group number
        while True:
            curr_table_message('Group')
            view_groups_list(db_cursor)
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

        # Email
        while True:
            curr_table_message('Group')
            view_groups_list(db_cursor)
            self.group_email = input('Enter group email: ')
            if re.match(r"""(?:[a-z0-9!#$%&'*+ /=?^_`{ | }~-]+(?: \.[a-z0-9!  # $%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
                        self.group_email):
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

        try:
            db_cursor.execute(
                f"""INSERT INTO groups_table(group_num, group_email)
                    VALUES( "{self.group_num}", "{self.group_email}" )
                """
            )
            print('\nData saved...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not saved to the table, possible reasonses:
                    
                    * The group number or email address isn't unique (they must be unique)
                """
            )

    def delete_row(self, db_cursor) -> None:
        """Delete row from the table"""
        group_id = 0

        screen_clear()

        # Group ID
        while True:
            view_groups_list(db_cursor)
            try:
                group_id = int(input('Enter group id number: '))
            except ValueError:
                print('Error: enter group id (number > or = 1) again...')
                continue
            else:
                if 1 <= group_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter group id (number > or = 1) again...')
                continue

        try:
            db_cursor.execute(
                f"""DELETE FROM groups_table WHERE group_id = {group_id}
                """
            )
            print('\nData deleted...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not deleted from the table, possible reasons:

                    * The group with the entered group ID doesn't exist
                    * The groups_table is empty
                """
            )

    def edit_row(self, db_cursor) -> None:
        """Edit row in the table"""

        # Identification of data in need of change by adding variable names
        # Data in the list must match the names of fields in the table
        changing_data = []
        group_id = 0

        # Group id
        while True:
            screen_clear()
            view_groups_list(db_cursor)
            try:
                group_id = int(input('Enter group id number: '))
            except ValueError:
                print('Error: enter group id (number > or = 1) again...')
                continue
            else:
                if 1 <= group_id:
                    option = data_save_option()
                    if option == 1:
                        break
                    elif option == 0:
                        continue
                    else:
                        continue
                print('Error: enter group id (number > or = 1) again...')
                input('Press enter to continue...')
                continue

        # Editing row by selected ID
        # Group number
        while True:
            screen_clear()
            view_groups_list(db_cursor)
            self.group_num = input(
                "Enter group number (or press enter if you don't want to change the data): ")
            if self.group_num == '':
                break
            if re.match(r'^\d{1,10}$', self.group_num):
                option = data_save_option()
                if option == 1:
                    changing_data.append('group_num')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter group number (no more than 10 characters) again...')

        # Email
        while True:
            screen_clear()
            view_groups_list(db_cursor)
            self.group_email = input(
                "Enter group email (or press enter if you don't want to change the data): ")
            if self.group_email == '':
                break
            if re.match(r"""(?:[a-z0-9!#$%&'*+ /=?^_`{ | }~-]+(?: \.[a-z0-9!  # $%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
                        self.group_email):
                option = data_save_option()
                if option == 1:
                    changing_data.append('group_email')
                    break
                elif option == 0:
                    continue
                else:
                    continue
            else:
                print(
                    'Error: Inccorect input, please enter email (no more than 70 characters) again...')

        try:
            if len(changing_data) != 0:
                sets_in_sql_query = []

                if 'group_num' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        group_num = "{self.group_num}"
                        """
                    )

                if 'group_email' in changing_data:
                    sets_in_sql_query.append(
                        f"""
                        group_email = "{self.group_email}"
                        """
                    )

                db_cursor.execute(
                    f"""UPDATE groups_table
                        SET {','.join(sets_in_sql_query)}
                        WHERE group_id = {group_id}
                    """
                )
                print('\nData edited...\n')
            else:
                print('\nData not edited...\n')
        except OperationalError or IntegrityError:
            print(
                """Error: the data is not edited in the table, possible reasons:

                    * The group with the entered group ID doesn't exist
                    * The groups_table is empty
                    * The group number or email address isn't unique (they must be unique)
                """
            )
