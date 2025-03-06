from schoolapp.src.schoolapp import instructor
from schoolapp.src.schoolapp.user import User

class Student(User):
    def __init__(self, name ,email , password, student_id):
        super().__init__(name,email,password)
        self.student_id = student_id
        self.students = []
        self.is_logged_in = False

    def register_student(self, name ,email , password, student_id, courses):
        self.students.append(name,email,password,student_id)
        self.is_logged_in = True

    def enroll(self,course_level , course_name, course_code):
        if self.is_logged_in == False:
            raise Exception("Student is not logged in")
        for course in instructor.Instructor.get_courses(self):
            if course.name == course_name:
                return"registerd sucessfully'"


    def login(self, email, password):
        if email and password in self.students:
            self.is_Loged_in = True
            return "login successful"
        return "login unsuccessful try again"








