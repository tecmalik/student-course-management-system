import sys


from email_validator import EmailNotValidError

from schoolapp.exception.exceptions import InvalidLoginException, PasswordNotAccepted, CourseAlreadyExist
from schoolapp.src.schoolapp.instructors import Instructors




email = ""
password = ""
Instructor = []
student = []
prompt = """
        Welcome
        1. Login
        2. Register
        3. Exit
    """

registration_prompt = """
        1. register as An instructor
        2. register as A student
    """
instructor_prompt = """
        1. Create Courses
        2. View Created Courses Instructor
        3. View Created Courses
        4. Assign Grades To Student
        5. View Registered Students
        6. Exit
    """

student_prompt = """
        1. View Available Courses
        2. Enroll For A Course
        3. View course Grades  
        4. view Enrolled course
        5. Exit
        """

registration_status = """
        1. register as Instructor
        2. Register as Student
        4. Exit
"""

def user_choice(message):
    return input(message)

def display(message):
    print(message)


def create_courses():
    course_name = user_choice("Enter courses name")
    course_code = user_choice("Enter course code")
    try:
        instructor = Instructors.find_by_email(email)
        instructor.create_course(course_name, course_code)
    except InvalidLoginException as e :
        display(e)
    except CourseAlreadyExist as e :
        display(e)
    finally:
        instructor_memu()


def view_created_courses_instructor():
    pass


def instructor_memu():
    user_input = user_choice(instructor_prompt)
    match(user_input):
        case '1': create_courses()
        case '2': view_created_courses_instructor()
        case '3': view_created_courses()
        case '4': view_registered_students()
        case '5': assign_grades_to_Student()
        case '6': sys.exit(0)
        case _ :
            display('Invalid choice')
            instructor_memu()


def student_menu():
    user_input = user_choice(student_prompt)
    match(user_input):
        case '1' : view_available_courses()
        case '2' : enroll_for_a_course()
        case '3' : view_course_rades()
        case '4' : view_enrolled_course()
        case '5' : sys.exit(0)
        case _ :
            display("invalid choice")
            student_menu()


def register_user():
    first_name = user_choice("Enter First Name : ")
    last_name = user_choice("Enter Last Name :")
    email = user_choice("Enter Email : ")
    password = user_choice("Enter password : ")
    user_input = user_choice(registration_status)
    match(user_input):
        case'1':
            try:
                Instructors.register(email, password, first_name, last_name)
            except InvalidLoginException as e:
                display(e)
            except PasswordNotAccepted as e :
                display(e)
            except EmailNotValidError as e:
                display(e)
            finally:
                user_login()

        case '2':
            try:
                Student(email, password,first_name,last_name)

            except InvalidLoginException as e:
                display(e)
            except PasswordNotAccepted as e:
                display(e)
            except EmailNotValidError as e:
                display(e)
            finally:
                student_login()
        case '3': sys.exit(0)


def login_Instructor():
    pass



def user_login():
    email = user_choice("Enter user Login :")
    password = user_choice("Enter password :")
    user_id = user_choice("Enter user ID :")
    try:
        alpha , number = user_id.split('-')
        display(alpha.upper())
        match(alpha.upper()):
            case 'I':login_Instructor()
            case 'S' :login_student()
            case _ : user_login()
    except InvalidLoginException as e :
        display(e);
    except ValueError as e :
        display(f" {e} \n Enter a Valid I.D")






def first_menu():
    user_input = user_choice(prompt)
    match(user_input):
        case '1' :
            user_login()
        case '2' :
            register_user()
        case '3' : sys.exit(0)
        case _ : first_menu()





first_menu()