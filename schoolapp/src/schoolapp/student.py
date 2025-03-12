from schoolapp.src.schoolapp.user import User

class Student(User):
    def __init__(self, email:str, password:str, first_name: str, last_name: str):
        super().__init__(first_name, last_name, email, password)
        self.email = email
        self.password = password
        self.student_id = self.student_id()
        self.enrolled_courses = []
        Student.count += 1

    count = 0
    @staticmethod
    def student_id():
        return f"S-0{Student.count}"

    def view_available_courses(self ,courses):
        print("Available Courses:")
        for course in courses:
            print(course)

    def register_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"Registered for course: {course}")
        else:
            print(f"Already enrolled in {course}")

    def view_registered_courses(self):
        print("Registered Courses:")
        if self.enrolled_courses:
            for course in self.enrolled_courses:
                print(course)
        else:
            print("No courses registered.")

    def view_grade(self):
        print("Grades are not yet implemented.")

    def unregister_a_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print(f"Unregistered from course: {course}")
        else:
            print(f"Not enrolled in {course}")

