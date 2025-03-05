import bcrypt

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


def login():
    pass


def first_menu():
    match userInput(prompt):
        case '1': login()
        case '2': registration_menu()
        case _ :
            print('invalid input')
            first_menu()

def registration_menu():
    match userInput(registration_prompt):
        case '1': register_instructor()
        case '2': register_student()
        case _ : 
            print('invalid input')
            registration_menu()


def instructors_menu():
    match userInput(registration_prompt):
        case '1': create_courses()
        case '2': view_created_courses()
        case '3': assign_grades_to_Student()
        case '4': view_registered_students()
        case _ :
            print('invalid input')
            instructors_menu()