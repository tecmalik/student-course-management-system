from abc import ABC


from schoolapp.src.schoolapp.user import  User

count = 0

def instructor_id():
    global count
    count += 1
    return f"T-{count}"

class Instructor(User):
    def __init__(self, name: str, email: str, password: str):
        super().__init__(name, email, password)
        self._created_courses = []
        self._instructor_id = instructor_id()

    @property
    def get_id(self):
        return self._instructor_id

    def create_course(self, name):
        pass


    def generate_id(self):
        return "I-" + str(self._instructor_id)


    def login(self, email, password):
        if email == self._email and password == self.__password:
            return True
        else:
            raise Exception("Invalid credentials")