import sqlite3

def view_student_lists(db_cursor) -> None:
    print('\n<--- Student list --->\n')
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
            f'id: {student_id}, first name: {first_name}, last name: {last_name}, email: {email},',
            f'date of birth: {date_of_birth}, course: {course}, group: {group_num}\n'
        )
    input('Press enter to continue... ')


def view_teacher_lists(db_cursor) -> None:
    print('\n<--- Teacher list --->\n')
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
            f'id: {teacher_id}, first name: {first_name}, last name: {last_name}, email: {email},',
            f'leads the subject: {subject_name}\n'
        )
    input('Press enter to continue... ')


def view_group_lists(db_cursor) -> None:
    print('\n<--- Group list --->\n')
    for row in db_cursor.execute(
    """
    SELECT group_id, group_num, group_email
    FROM groups_table 
    ORDER BY group_num
    """
    ):
        group_id, group_num, group_email = row
        print(f'id: {group_id}, group: {group_num}, group email: {group_email}\n')
    input('Press enter to continue... ')

def view_subject_lists(db_cursor) -> None:
    print('\n<--- Subject list --->\n')
    for row in db_cursor.execute(
    """
    SELECT subject_id, subject_name 
    FROM subjects 
    ORDER BY subject_name
    """
    ):
        subject_id, subject_name = row
        print(f'id: {subject_id}, name: {subject_name}\n')
    input('Press enter to continue... ')


def view_list(option, db_path) -> None:
    """ Viewing the list depending on option """

    options = {
        '1': view_student_lists,
        '2': view_teacher_lists,
        '3': view_group_lists,
        '4': view_subject_lists
    }
    
    db_connect = sqlite3.connect(db_path)
    db_cursor = db_connect.cursor()

    view_func = options[str(option)]
    view_func(db_cursor)

    db_connect.close()