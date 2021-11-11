import sqlite3

def view_list(option, db_path) -> None:
    """ Viewing the list depending on option """

    options = {
        1: view_students_list,
        2: view_teachers_list,
        3: view_groups_list,
        4: view_subjects_list,
        5: view_assessments_list
    }

    db_connect = sqlite3.connect(db_path)
    db_cursor = db_connect.cursor()

    view_func = options[option]
    view_func(db_cursor)

    db_connect.close()

def table_is_empty(table_name: str, db_cursor) -> bool:
    """Return True if table is empty or False if it's not"""

    # Returns sqlite3.Cursor object which needs to be converted to tuple
    # If tuple is equal (0,) - table is empty otherwise it's not
    sql_cursor_obj = db_cursor.execute(f'SELECT COUNT(*) AS IsEmpty FROM {table_name}')
    tuple_obj, = sql_cursor_obj
    if not tuple_obj[0]:
        print('Table is empty\n')
        return True
    else:
        return False

def view_students_list(db_cursor) -> None:
    print('\n<--- Students list --->\n')

    if table_is_empty('students', db_cursor):
        return
    else: 
        for row in db_cursor.execute(
            """
            SELECT student_id, first_name, last_name, email, date_of_birth, course, group_num 
            FROM students 
                INNER JOIN groups_table USING(group_id) 
            ORDER BY first_name
            """
        ):
            student_id, first_name, last_name, email, date_of_birth, course, group_num = row
            print(
                f'id: {student_id}, name: {first_name} {last_name}, email: {email},',
                f'date of birth: {date_of_birth}, course: {course}, group: {group_num}'
            )
        print('')

def view_teachers_list(db_cursor) -> None:
    print('\n<--- Teachers list --->\n')

    if table_is_empty('teachers', db_cursor):
        return
    else:
        for row in db_cursor.execute(
            """
            SELECT teacher_id, first_name, last_name, email, subject_name
            FROM teachers
                INNER JOIN subjects USING(subject_id)  
            ORDER BY first_name
            """
        ):
            teacher_id, first_name, last_name, email, subject_name = row
            print(
                f'id: {teacher_id}, name: {first_name} {last_name}, email: {email},',
                f'leads the subject: {subject_name}'
            )
        print('')

def view_groups_list(db_cursor) -> None:
    print('\n<--- Groups list --->\n')
    
    if table_is_empty('groups_table', db_cursor):
        return
    else:
        for row in db_cursor.execute(
            """
            SELECT group_id, group_num, group_email
            FROM groups_table 
            ORDER BY group_num
            """
        ):
            group_id, group_num, group_email = row
            print(f'id: {group_id}, group: {group_num}, group email: {group_email}')
        print('')

def view_subjects_list(db_cursor) -> None:
    print('\n<--- Subjects list --->\n')

    if table_is_empty('subjects', db_cursor):
        return
    else:
        for row in db_cursor.execute(
            """
            SELECT subject_id, subject_name 
            FROM subjects 
            ORDER BY subject_name
            """
        ):
            subject_id, subject_name = row
            print(f'id: {subject_id}, name: {subject_name}')
        print('')

def view_assessments_list(db_cursor) -> None:
    print('\n<--- Assessments list --->\n')

    if table_is_empty('subject_assessments', db_cursor):
        return
    else:
        for row in db_cursor.execute(
            """
            SELECT assessment_id, assessment, first_name, last_name, subject_name, date 
            FROM students
                INNER JOIN subject_assessments USING(student_id)
                INNER JOIN subjects USING(subject_id)
            ORDER BY first_name, last_name
            """
        ):
            assessment_id, assessment, first_name, last_name, subject_name, date = row
            print(f'id: {assessment_id}, name: {first_name} {last_name},',
                f'assessment: {assessment}, subject name: {subject_name}, date: {date}')
        print('')