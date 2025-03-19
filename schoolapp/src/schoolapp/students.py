from schoolapp.exception.exceptions import StudentAlreadyRegistered, InvalidLoginException
from schoolapp.src.schoolapp.student import Student


class Students:
    def __init__(self):
        self.students = []


    def register(self, firstname , lastname, email ,password ):
        for student in self.students:
            if student.email == email :
                raise StudentAlreadyRegistered("student already registered")
        registered_student = Student(firstname, lastname, email, password)
        self.students.append(registered_student)


    def login(self,email,password):
        for student in self.students:
            if student.email == email :
                student.login_user(email, password)

    def find_by_email(self,email):
        for student in self.students:
            if student.email == email :
                return student
        raise InvalidLoginException("Invalid email or password")

    def find_by_id(self,student_id):
        for student in self.students:
            if student.student_id()== student_id :
                return student
        raise InvalidLoginException("invalid Id")
