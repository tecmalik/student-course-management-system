from schoolapp.exception.exceptions import InstructorAlreadyRegistered, InvalidLoginException
from schoolapp.src.schoolapp.instructor import Instructor



class Instructors:
    def __init__(self):
        self.instructors = []

    def register(self, firstname, lastname, email, password):
        for instructor in self.instructors:
            if instructor.email == email:
                raise InstructorAlreadyRegistered("student already registered")
        registered_instructor = Instructor(firstname, lastname, email, password)
        self.instructors.append(registered_instructor)

    def login(self,email,password):
        for instructor in self.instructors:
            if instructor.email == email :
                instructor.login_user(email, password)
        raise InvalidLoginException("Invalid email or password")

    def find_by_email(self, email):
        for instructor in self.instructors:
            if instructor.email == email :
                return instructor
        raise InvalidLoginException("Invalid email or password")

    def find_by_instructor_id(self,instructor_id):
        for instructor in self.instructors:
            if instructor.instructor_id == instructor_id :
                return instructor
        raise InvalidLoginException("Invalid Id")

