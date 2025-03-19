from schoolapp.exception.exceptions import InstructorAlreadyRegistered, InvalidLoginException
from schoolapp.src.schoolapp.instructor import Instructor



class Instructors:

    def __init__(self):
        self.instructors:[Instructor]= []

    def register(self, firstname, lastname, email, password):
        for instructor in self.instructors:
            if instructor.get_email == email:
                raise InstructorAlreadyRegistered("instructor already registered")
        registered_instructor = Instructor(firstname, lastname, email, password)
        self.instructors.append(registered_instructor)
        print("registered successfully")

    def login(self,email,password):
        for instructor in self.instructors:
            if instructor.get_email == email :
                instructor.login_user(email, password)
                print('login successfully')
        raise InvalidLoginException("Invalid email or password")



    def find_by_email(self, email):
        for instructor in self.instructors:
            if instructor.get_email == email :
                return instructor
        raise InvalidLoginException("Invalid email or password")

    def find_by_instructor_id(self,instructor_id):
        for instructor in self.instructors:
            if instructor.instructor_id == instructor_id :
                return instructor
        raise InvalidLoginException("Invalid Id")

    def get_instructors_size(self):
        return  len(self.instructors)

