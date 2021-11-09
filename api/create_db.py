import sqlite3

def create_db(db_path) -> None:
    """Creates students, groups, subject_assessments, teachers and subjects table"""

    db_connect = sqlite3.connect(db_path)
    db_cursor = db_connect.cursor()
    
    # Create students table
    db_cursor.execute(
        """CREATE TABLE students (
	        student_id integer PRIMARY KEY AUTOINCREMENT,
	        first_name varchar(25),
	        last_name varchar(25),
	        email varchar(70) UNIQUE,
	        date_of_birth DATETIME,
	        course integer,
	        group_id integer,
            FOREIGN KEY (group_id) REFERENCES groups_table (group_id) ON DELETE SET NULL
        );"""
    )

    # Create groups table
    db_cursor.execute(
        """CREATE TABLE groups_table (
	        group_id integer PRIMARY KEY AUTOINCREMENT,
	        group_num integer,
            group_email varchar(70) UNIQUE
        );"""
    )

    # Create subject_assessments table
    db_cursor.execute(
        """CREATE TABLE subject_assessments (
	        assessment_id integer PRIMARY KEY AUTOINCREMENT,
	        assessment integer,
	        student_id integer,
	        subject_id integer,
	        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE,
            FOREIGN KEY (subject_id) REFERENCES subjects (subject_id) ON DELETE CASCADE
        );"""
    )
    
    # Create teachers table
    db_cursor.execute(
        """CREATE TABLE teachers (
	        teacher_id integer PRIMARY KEY AUTOINCREMENT,
	        first_name varchar(25),
	        last_name varchar(25),
	        email varchar(70) UNIQUE,
	        subject_id integer,
            FOREIGN KEY (subject_id) REFERENCES subjects (subject_id) ON DELETE SET NULL
        );"""
    )

    # Create subjects table
    db_cursor.execute(
        """CREATE TABLE subjects (
	        subject_id integer PRIMARY KEY AUTOINCREMENT,
	        subject_name varchar(100)
        );"""
    )

    db_connect.close()
