import bcrypt

from schoolapp.src.schoolapp.instructor import Instructor
from schoolapp.src.schoolapp.student import Student

prompt = """
    Welcome
    1. login
    2.register
"""
registration_prompt= """
    1. register as An instructor
    2. register as A student
"""
instructor_prompt = """
    1. create courses
    2. view created courses instructor
    3. assign grades to Student
    4. view registered students
"""

def userInput(prompt):
    return input(prompt)


student_prompt = """
    1. enroll for a course
    2. view available courses
    3. view grades  
    """


def instructor_login():
    try:
        userInput("Enter username to login: ")
        userInput("Enter password to login: ")

    except Exception as err :
        print(err)
    finally:
        instructors_menu()




def first_menu():
    match userInput(prompt):
        case '1': login()
        case '2': registration_menu()
        case _ :
            print('invalid input')
            first_menu()


def register_student():
    email = userInput("Enter email to register: ")
    name = userInput("Enter name to register: ")
    password = userInput("Enter password to register: ")
    student_id =userInput("Enter student ID (S###) to register: ")
    try:
        student = Student(email, name, password,student_id)
        print('student registered successfully')
        
    except ValueError as err:
        print(err)
    finally: 
        student_menu()


def register_instructor():
    name = userInput("Enter name to register: ")
    email = userInput("Enter email to register: ")
    password = userInput("Enter a password: ")
    instructor_id = userInput("Enter instructor ID (I###): ")
    try :
        instructor = Instructor(email, name, password,instructor_id)
        print('instructor registered successfully')
    except ValueError as err:
        print(err)
    finally: 
        instructors_menu()


def registration_menu():
    match userInput(registration_prompt):
        case '1': register_instructor()
        case '2': register_student()
        case _ :
            print('invalid input')
            registration_menu()


def create_courses():
    email = input("Enter email to register: ")
    Student = Student(email,"password","Student","S0001")



def instructors_menu():
    match userInput(registration_prompt):
        case '1': create_courses()
        case '2': view_created_courses()
        case '3': assign_grades_to_Student()
        case '4': view_registered_students()
        case _ :
            print('invalid input')
            instructors_menu()



