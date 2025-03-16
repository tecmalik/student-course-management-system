from schoolapp.exception.exceptions import StudentAlreadyRegistered
from schoolapp.src.schoolapp.student import Student


class Students:
    def __init__(self):
        self.students = []


    def register(self, firstname , lastname, email ,password ):
        for student in self.students:
            if student.email == email :
                raise StudentAlreadyRegistered("student already registered")
             = Student(firstname, lastname, email, password)
        self.students.append(student)

    def login(self,email,password):
        for student in self.students:
            if student.email == email :
                student.login(email,password)
