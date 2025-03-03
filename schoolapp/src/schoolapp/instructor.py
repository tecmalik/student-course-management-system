
from schoolapp.src.schoolapp.user import  User

count = 0
def instructor_id():
    count += 1
    return F" T-{count}"

class Instructor(User):
    def __init__(self, name ,email,password, instructor_id, subject):
        super().__init__(name,email,password)
        self._instructor_id = instructor_id

