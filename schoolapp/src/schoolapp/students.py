
from schoolapp.src.schoolapp.student import Student


class Students:
    def __init__(self):
        self.students = []

    def register_students(self, firstname , lastname, email ,password ):
        for student in self.students:
            if student.first_name == firstname and student.last_name == lastname:
                raise StudentAlreadyRegistered("student already registered")
        student.append(Student(firstname,lastname,email,password))
