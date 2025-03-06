<<<<<<< HEAD
from schoolapp.src.schoolapp.course import Course
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



    def create_course(self, course_name, course_id):
        course = Course(course_name, course_id, self)
        self._created_courses.append(course)
        return course

    def get_id(self):
        return self._instructor_id



    def generate_id(self):
        return "I-" + str(self._instructor_id)


    def login(self, email, password):
        if email == self._email and password == self.__password:
            return True
        else:
            raise Exception("Invalid credentials")


    def view_students_in_course(self,course):
        if not course in self._created_courses:
            return  [student.name for student in course.enrolled_students]

    def assign_grade(self, student, course, grade):
        if course in self._created_courses:
            if student in course.enrolled_students:
                print(f"Grade {grade} assigned to {student.name} for {course.course_name}.")
            else:
                raise ValueError("Student is not enrolled in this course.")
        else:
            raise ValueError("You can only assign grades for courses you created.")
=======

>>>>>>> c9d514e8cc8721591aebd0b4d42bc0eb06435b9b
