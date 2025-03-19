import sys


from email_validator import EmailNotValidError

from schoolapp.exception.exceptions import InvalidLoginException, PasswordNotAccepted, CourseAlreadyExist, \
    InvalidArgumentException
from schoolapp.src.schoolapp.instructors import Instructors
from schoolapp.src.schoolapp.students import Students

email = " "
password = " "
instructors = Instructors()
students = Students()

prompt = """
        Welcome
        1. Login
        2. Register
        3. Exit
    """

registration_prompt = """
        1. register as Instructor
        2. register as student
        3. Back 
        4. Exit
    """
instructor_prompt = """
        1. Create Courses
        2. View Created Courses Instructor
        3. View Created Courses
        4. Assign Grades To Student
        5. View Registered Students
        6. Back to main menu
        7. Exit
    """

student_prompt = """
        1. View Available Courses
        2. Enroll For A Course
        3. View course Grades  
        4. view Enrolled course
        5. Back to main menu
        6. Exit
        """


def user_options(message):
    return input(message)

def display(message):
    return print(message)


def create_courses():
    course_name = user_options("Enter courses name")
    course_code = user_options("Enter course code")
    instructor = instructors.find_by_email(email)
    instructor.create_course(course_name , course_code)
    try:
        instructor = instructors.find_by_email(email)
        instructor.create_course(course_name, course_code)
    except InvalidLoginException as e :
        display(e)
    except CourseAlreadyExist as e :
        display(e)
    except Exception as e :
        display(e)
    finally:
        instructor_memu()


def view_created_courses_instructor():
    course_name = user_options("Enter course name : ")
    course_id = user_options("Enter course id : ")

    try:
        instructor = instructors.find_by_email(email)
        instructor.create_course(course_name, course_id)
    except EmailNotValidError as e :
        display (e)
    except InvalidLoginException as e :
        display (e)
    except Exception as e:
        display(e)
    finally :
        instructor_memu()


def instructor_memu():
    user_input = user_options(instructor_prompt)
    match(user_input):
        case '1': create_courses()
        case '2': view_created_courses_instructor()
        case '3': view_created_courses()
        case '4': view_registered_students()
        case '5': assign_grades_to_Student()
        case '6': first_menu()
        case '7': sys.exit(0)
        case _ :
            display('Invalid choice')
            instructor_memu()


def student_menu():
    user_input = user_options(student_prompt)
    match(user_input):
        case '1' : view_available_courses()
        case '2' : enroll_for_a_course()
        case '3' : view_course_rades()
        case '4' : view_enrolled_course()
        case '5' : first_menu()
        case '6' : sys.exit(0)
        case _ :
            display("invalid choice")
            student_menu()


def register_user():
    user_input = user_options(registration_prompt)
    first_name:str = user_options("Enter First Name : ")
    last_name:str = user_options("Enter Last Name :")
    email:str = user_options("Enter Email : ")
    password:str = user_options("Enter password : ")

    match(user_input):
        case'1':
            try:
                instructors.register (first_name, last_name,email, password, )
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
                students.register(first_name,last_name,email, password)
            except InvalidLoginException as e:
                display(e)
            except PasswordNotAccepted as e:
                display(e)
            except EmailNotValidError as e:
                display(e)
            except Exception as e:
                display(e)
            finally:
                user_login()
        case '3': first_menu()
        case '4' : sys.exit(0)
        case _ : display("Invalid input. input a number 1 to five ")



def user_login():
    email = user_options("Enter user Login :")
    password = user_options("Enter password :")
    user_id = user_options("Enter user ID :")
    try:
        alpha , number = user_id.split('-')
        display(alpha.upper())
        match(alpha.upper()):
            case 'I':
                try:
                    instructor = instructors.find_by_email(email)
                    instructor.login_user(email,password)
                except InvalidLoginException as e :
                    display(e)
                except EmailNotValidError as e :
                    display(e)
                except InvalidArgumentException as e :
                    display(e)
                finally:
                    user_login()

            case 'S' :
                try :
                    student = students.find_by_email(email)
                    student.login(email,password)
                except Exception as e :
                    display(e)
                except EmailNotValidError as e :
                    display(e)
            case _ : user_login()
    except InvalidLoginException as e :
        display(e);
    except ValueError as e :
        display(f" {e} \n Enter a Valid I.D")



def first_menu():
    user_input = user_options(prompt)
    match(user_input):
        case '1' :
            user_login()
        case '2' :
            register_user()
        case '3' : sys.exit(0)
        case _ : first_menu()





first_menu()