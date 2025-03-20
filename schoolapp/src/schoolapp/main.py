import sys


from email_validator import EmailNotValidError

from schoolapp.exception.exceptions import InvalidLoginException, PasswordNotAccepted, CourseAlreadyExist, \
    InvalidArgumentException, PasswordTooShort
from schoolapp.src.schoolapp.instructors import Instructors

from schoolapp.src.schoolapp.students import Students

class Main:
    def __init__(self):
        self.email = " "
        self.password = " "
        self.instructors = Instructors()
        self.students = Students()

    prompt = """
            STUDENT COURSE MANAGEMENT APP
            1. Login
            2. Register
            3. Exit
        """

    registration_prompt = """
            REGISTRATION MENU
            1. register as Instructor
            2. register as student
            3. Back 
            4. Exit
        """
    instructor_prompt = """
            INSTRUCTORS MENU
            1. Create Courses
            2. View Created Courses Instructor
            3. View Created Courses
            4. Assign Grades To Student
            5. View Registered Students
            6. Back to main menu
            7. Exit
        """

    student_prompt = """
            STUDENT MENU
            1. View Available Courses
            2. Enroll For A Course
            3. View course Grades  
            4. view Enrolled course
            5. Back to main menu
            6. Exit
            """


    def user_options(self,message):
        return input(message)


    def display(self,message):
        return print(message)


    def create_courses(self):
        course_name = self.user_options("Enter courses name")
        course_code = self.user_options("Enter course code")
        instructor = self.instructors.find_by_email(self.email)
        instructor.create_course(course_name , course_code)
        try:
            instructor = self.instructors.find_by_email(self.email)
            instructor.create_course(course_name, course_code)

        except InvalidLoginException as e :
            self.display(e)
        except CourseAlreadyExist as e :
            self.display(e)
        except ValueError as e :
            self.display(e)
        except Exception as e:
            self.display(e)
        finally:
            self.instructor_memu()


    def view_created_courses_instructor(self):
        course_name = self.user_options("Enter course name : ")
        course_id = self.user_options("Enter course id : ")

        try:
            instructor = self.instructors.find_by_email(self.email)
            instructor.view_created_courses(course_name, course_id)
        except EmailNotValidError as e :
            self.display (e)
        except InvalidLoginException as e :
            self.display (e)
        except Exception as e:
            self.display(e)
        finally :
            self.instructor_memu()


    def instructor_memu(self):
        user_input = self.user_options(self.instructor_prompt)
        match user_input:
            case '1': self.create_courses()
            case '2': self.view_created_courses_instructor()
            case '3': self.view_created_courses()
            case '4': self.view_registered_students()
            case '5': self.assign_grades_to_Student()
            case '6': self.first_menu()
            case '7': sys.exit(0)
            case _ :
                self.display('invalid input !!!, enter a valid choice 1-7')
                self.instructor_memu()


    def student_menu(self):
        user_input = self.user_options(self.student_prompt)
        match(user_input):
            case '1' : self.view_available_courses()
            case '2' : self.enroll_for_a_course()
            case '3' : self.view_course_rades()
            case '4' : self.view_enrolled_course()
            case '5' : self.first_menu()
            case '6' : sys.exit(0)
            case _ :
                self.display('invalid input !!!, enter a valid choice 1-6')
                self.student_menu()


    def register_user(self):
        users_input = self.user_options(self.registration_prompt)
        match users_input :
            case'1':
                try:
                    first_name: str = self.user_options("Enter First Name : ")
                    last_name: str = self.user_options("Enter Last Name :")
                    self.email: str = self.user_options("Enter Email : ")
                    self.password : str = self.user_options("Enter password : ")
                    self.instructors.register(first_name, last_name, self.email, self.password)
                    self.instructor = self.instructors.find_by_email(self.email)
                    self.display('registration successfully')
                    self.display(f"{self.instructor.get_email} Registered Successfully. \n your ID is : {self.instructor.get_instructor_id}")

                except InvalidLoginException as e:
                    self.display(e)
                except PasswordTooShort as e:
                    self.display(e)
                except PasswordNotAccepted as e :
                    self.display(e)
                except EmailNotValidError as e:
                    self.display(e)
                except ValueError as e:
                    self.display(e)
                finally:
                    self.register_user()

            case '2':

                try:
                    student_first_name: str = self.user_options("Enter First Name : ")
                    last_name: str = self.user_options("Enter Last Name :")
                    self.email: str = self.user_options("Enter Email : ")
                    self.password: str = self.user_options("Enter password : ")
                    self.students.register(student_first_name,last_name,self.email, self.password)
                    self.student = self.students.find_by_email(self.email)
                    self.display(f"your ID is : {self.student.get_student_id}")

                except InvalidLoginException as e:
                    self.display(e)
                except PasswordNotAccepted as e:
                    self.display(e)
                except EmailNotValidError as e:
                    self.display(e)
                except PasswordTooShort as e:
                    self.display(e)
                except ValueError as e:
                    self.display(e)
                finally:
                    self.register_user()
            case '3': self.first_menu()
            case '4' : sys.exit(0)
            case _ :
                self.display("Invalid input. input a number 1 to 4")
                self.first_menu()

    def user_login(self):
        self.email = self.user_options("Enter email :")
        self.password = self.user_options("Enter password :")
        user_id = self.user_options("Enter user ID :")
        try:
            alpha , number = user_id.split('-')
            match alpha.upper() :
                case 'I':
                    try:
                        instructor = self.instructors.find_by_email(self.email)
                        instructor.login_user(self.email,self.password)
                    except InvalidLoginException as e :
                        self.display(e)
                    except EmailNotValidError as e :
                        self.display(e)
                    except InvalidArgumentException as e :
                        self.display(e)
                    finally:
                        self.user_login()

                case 'S' :
                    try :
                        student = self.students.find_by_email(self.email)
                        student.login(self.email,self.password)
                    except Exception as e :
                        self.display(e)
                    except EmailNotValidError as e :
                        self.display(e)
                case _ :
                    self.user_login()
        except InvalidLoginException as e :
            self.display(e);
        except ValueError as e :
            self.display(f" {e} \n Enter a Valid I.D")
        finally:
            self.first_menu()



    def first_menu(self):
        user_input = self.user_options(self.prompt)
        match user_input :
            case '1' :
                self.user_login()
            case '2' :
                self.register_user()
            case '3' : sys.exit(0)
            case _ :
                self.display('invalid input !!!, enter a valid choice 1-3')
                self.first_menu()

    def view_available_courses(self):
        pass


Main().first_menu()