import re

from src.schoolapp import course
from src.schoolapp.user import User

def validate_password(password):
    pattern = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
    if re.match(pattern, password):
        return password
    else:
        raise Exception("Invalid password")


def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return email
    else:
        raise Exception("Invalid email")

def validate_student_ID(student_id):
    pattern = r"^[0-9]{8}$"
    if re.match(pattern, student_id):
        return student_id
    else:
        raise Exception("Invalid student ID")

class Student(User):
    def __init__(self, name ,email , password, student_id):
        super().__init__(name,email,password)
        self.student_id = validate_student_ID(student_id)
        self.enrolled_courses = []

    def view_available_courses(self, courses):
        return [courses.course_name for courses in courses]

    def enroll_course(self, course):
        if course.course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course.course_name)
            course.enrolled_courses.append(self)

    def view_enrolled_courses(self, courses):
        return [course.course_name for courses in courses]

    def view_grade(self):
        return [course.course_name: course.get_grade() for course in self.enrolled_courses]




