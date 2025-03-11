from schoolapp.exception.exceptions import CourseAlreadyExist, CourseDoesNotExist
from schoolapp.src.schoolapp.user import User


class Instructor(User):
    count = 1

    def __init__(self, email:str,  password:str, first_name: str, last_name: str):

        super().__init__(first_name, last_name, email, password)
        self.instructor_id = self.instructor_id()
        self.created_courses = []
        self.students_in_courses = {}
        Instructor.count += 1


    @staticmethod
    def instructor_id():
        return f"I-0{Instructor.count}"

    @property
    def get_instructor_id(self):
        return self.instructor_id

    def get_number_of_created_courses(self):
        return len(self.created_courses)

    def create_course(self, course_name, course_id):
        for course in self.created_courses:
            if course['name'] == course_name and course['id'] == course_id:
                raise CourseAlreadyExist(f'{course_name} already exists')
        course = {"name": course_name, "id": course_id}
        self.created_courses.append(course)
        self.students_in_courses[course_id] = []
        print(f"Course '{course_name}' created successfully!")

    def delete_course(self, course_name, course_id):
        if len(self.created_courses) == 0 :
            raise CourseDoesNotExist(f"{course_name} doesn't exist")
        for course in self.created_courses:
            if course["name"] == course_name and course["id"] == course_id:
                self.created_courses.remove(course)
        print(f"Course '{course_name}' deleted successfully!")

    def view_students_in_course(self, course_id):
        if course_id in self.students_in_courses:
            students = self.students_in_courses[course_id]
            print(f"Students in course ID {course_id}: {students if students else 'No students enrolled yet.'}")
        else:
            print(f"No such course with ID {course_id} exists.")

    def assign_grades(self, course_id, student_name, grade):
        if course_id in self.students_in_courses:
            if student_name in self.students_in_courses[course_id]:
                print(f"Assigned grade '{grade}' to student '{student_name}' in course ID {course_id}.")
                # Extend this to store grades if needed.
            else:
                print(f"Student '{student_name}' not found in course ID {course_id}.")
        else:
            print(f"No such course with ID {course_id} exists.")


    def view_created_courses(self):
        print("Created courses:")
        for course in self.created_courses:
            print(f"Course Name: {course['name']}, Course ID: {course['id']}")
        if not self.created_courses:
            print("No courses created yet.")

    def view_students_and_grades(self, course_id):
        if course_id in self.students_in_courses:
            print(f"Students and grades for course ID {course_id}:")
            for student in self.students_in_courses[course_id]:
                print(f"- {student}: [Grade Not Implemented Yet]")
        else:
            print(f"No such course with ID {course_id} exists.")

