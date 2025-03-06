from schoolapp.src.schoolapp import course
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
        self._instructor_id = instructor_id
        self.instructors = []

    def get_courses(self):
        return self._created_courses

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

    def view_students_in_course(self):
        if not course in self._created_courses:
            return [student.name for student in course.enrolled_students]

    def assign_grade(self, student, grade):
        if course in self._created_courses:
            if student in course.enrolled_students:
                print(f"Grade {grade} assigned to {student.name} for {course.course_name}.")
            else:
                raise ValueError("Student is not enrolled in this course.")

        else:
            raise ValueError("You can only assign grades for courses you created.")