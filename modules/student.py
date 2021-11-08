import sqlite3

class Student():
    def __init__(self, first_name: str, last_name: str, email: str, date_of_birth: str, group: int, course: int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.group = group
        self.course = course

        db_connect = sqlite3.connect('../db.sqlite3')
        db_connect.close()
    
    def __str__(self):
        return f"Student: {self.name}, group: {str(self.group)}, course: {str(self.course)}"