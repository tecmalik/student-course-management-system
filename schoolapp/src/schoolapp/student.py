from schoolapp.exception.exceptions import NoCourseAvailableException, InvalidCourseDetails
from schoolapp.src.schoolapp.systemfilemanager import SystemFileManager
from schoolapp.src.schoolapp.user import User

class Student(User):
    system_file = SystemFileManager()
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

    def view_available_courses(self ):
        self.system_file.load_course('courses.json','course', self.enrolled_courses)
        if len(self.enrolled_courses) == 0:
            raise NoCourseAvailableException("no course available")
        return self.enrolled_courses

    def register_course(self, course_id:str):
        courses_list = self.view_available_courses()
        for courses in courses_list:
            if course_id == courses.course_id:
                self.enrolled_courses.append(courses)
                print(f"Registered for course: {courses.course_name} : {courses.course_id} successfully.")

        # raise InvalidCourseDetails(f"Already enrolled in {course_id}")

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



