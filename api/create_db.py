import sqlite3

def create_db(db_path) -> None:
    """Creates students, groups, subject_assessments, teachers and subjects table"""

    db_connect = sqlite3.connect(db_path)
    db_cursor = db_connect.cursor()
    
    # Create students table
    db_cursor.execute(
        """
        CREATE TABLE students (
            student_id    INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
            first_name    VARCHAR (25) NOT NULL,
            last_name     VARCHAR (25) NOT NULL,
            email         VARCHAR (70) UNIQUE NOT NULL,
            date_of_birth DATETIME     NOT NULL,
            course        INTEGER      NOT NULL,
            group_id      INTEGER      NOT NULL,
            FOREIGN KEY (
                group_id
            )
            REFERENCES groups_table (group_id) ON DELETE NO ACTION
        );
        """
    )

    # Create groups table
    db_cursor.execute(
        """
        CREATE TABLE groups_table (
            group_id    INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
            group_num   VARCHAR (10) UNIQUE NOT NULL,
            group_email VARCHAR (70) UNIQUE NOT NULL
        );
        """
    )

    # Create subject_assessments table
    db_cursor.execute(
        """
        CREATE TABLE subject_assessments (
            assessment_id INTEGER   PRIMARY KEY AUTOINCREMENT NOT NULL,
            assessment    INTEGER   NOT NULL,
            student_id    INTEGER   NOT NULL,
            subject_id    INTEGER   NOT NULL,
            date          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (
                student_id
            )
            REFERENCES students (student_id) ON DELETE CASCADE,
            FOREIGN KEY (
                subject_id
            )
            REFERENCES subjects (subject_id) ON DELETE CASCADE
        );
        """
    )
    
    # Create teachers table
    db_cursor.execute(
        """
        CREATE TABLE teachers (
            teacher_id INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
            first_name VARCHAR (25) NOT NULL,
            last_name  VARCHAR (25) NOT NULL,
            email      VARCHAR (70) UNIQUE NOT NULL,
            subject_id INTEGER      NOT NULL,
            FOREIGN KEY (
                subject_id
            )
            REFERENCES subjects (subject_id) ON DELETE NO ACTION
        );
        """
    )

    # Create subjects table
    db_cursor.execute(
        """
        CREATE TABLE subjects (
            subject_id   INTEGER       PRIMARY KEY AUTOINCREMENT NOT NULL,
            subject_name VARCHAR (100) NOT NULL UNIQUE
        );
        """
    )

    db_connect.close()
