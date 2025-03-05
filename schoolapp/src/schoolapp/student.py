from django.utils.timezone import override

from schoolapp.src.schoolapp.user import User


class Student(User):
    def __init__(self, name ,email , password, student_id):
        super().__init__(name,email,password)
        self.student_id = student_id


    @override
    def generate_id(self):
        pass

    @override
    def login(self, email, password):
        pass



