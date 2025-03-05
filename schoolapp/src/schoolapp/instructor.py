from schoolapp.exception.exceptions import ExistingLogInDetails
from schoolapp.src.schoolapp import course
from schoolapp.src.schoolapp.user import  User


class Instructor(User):
    def __init__(self, name: str, email: str, password: str,instructor_id:str):
        super().__init__(name, email, password)
        self._created_courses = []
        self._instructor_id = instructor_id
        self.is_logged_in = False
        self.instructors = []



    def get_courses(self):
        return self._created_courses

    @property
    def get_id(self):
        return self._instructor_id

    def create_course(self, course_name:str, course_code:str, course_level:str ,instructors_name:str):
        self._created_courses.append(course.Course(course_name,course_code, course_level,instructors_name))

    def register(self, email:str,password:str):
        details = [email, password]
        for instructor in self.instructors:
            if email in instructor:
                raise ExistingLogInDetails ("Email already registered")
        self.instructors.append(details)


    def get_number_of_created_courses(self):
        return len(self._created_courses)

    def generate_id(self):
        return "I-" + str(self._instructor_id)


    def login(self, email, password):
        if email == self._email and password == self.__password:
            return 'login Successful'
        else:
            raise Exception("Invalid credentials")

    def view_enrolled_student(self):
        studentList =[]
        for student in self._created_courses:
            if self.is_logged_in:
                studentList.append(student)
        return studentList