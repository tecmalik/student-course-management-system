from schoolapp.exception.exceptions import InvalidArgumentException
from schoolapp.src.schoolapp.user import User
from schoolapp.src.schoolapp.course import Course
import re


class Instructor(User):
    count = 0
    INSTRUCTOR_ID_PATTERN = r"^I-\d{3}$"

    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        super().__init__(first_name, last_name, email, password)
        self.instructor_id = self._generate_instructor_id()
        self.created_courses = []
        Instructor.count += 1

    @staticmethod
    def _generate_instructor_id():
        Instructor.count += 1
        return f"I-{Instructor.count:03d}"

    def create_course(self, course_name: str, course_id: str):
        if not course_name or course_name.strip() == "":
            raise InvalidArgumentException("Course name cannot be empty")

        if not course_id or course_id.strip() == "":
            raise InvalidArgumentException("Course ID cannot be empty")

        for course in self.created_courses:
            if course.course_id == course_id:
                raise InvalidArgumentException(f"You already have a course with ID {course_id}")

        course = Course(course_name, course_id, self.get_fullname())
        self.created_courses.append(course)
        return course

    def view_created_courses(self):
        if not self.created_courses:
            print("You haven't created any courses yet.")
            return []

        return self.created_courses

    def display_created_courses(self):
        courses = self.view_created_courses()
        if courses:
            print(f"\nCourses created by {self.get_fullname()}:")
            for i, course in enumerate(courses, 1):
                print(
                    f"{i}. {course.course_name} (ID: {course.course_id}) - Students enrolled: {course.number_of_student()}")

    def view_course_students(self, course_id: str):
        for course in self.created_courses:
            if course.course_id == course_id:
                if not course._enrolled_students:
                    print(f"No students enrolled in {course.course_name}.")
                    return []

                print(f"\nStudents enrolled in {course.course_name}:")
                for i, student in enumerate(course._enrolled_students, 1):
                    print(f"{i}. {student.get_fullname()} (ID: {student.student_id})")

                return course._enrolled_students

        print(f"Course with ID {course_id} not found or not created by you.")
        return []

    def assign_grade(self, course_id: str, student_id: str, grade: str):
        for course in self.created_courses:
            if course.course_id == course_id:
                for student in course._enrolled_students:
                    if student.student_id == student_id:

                        print(f"Grade {grade} assigned to {student.get_fullname()} for course {course.course_name}")
                        return True

                print(f"Student with ID {student_id} not found in course {course.course_name}")
                return False

        print(f"Course with ID {course_id} not found or not created by you.")
        return False

    def remove_course(self, course_id: str):
        for course in self.created_courses:
            if course.course_id == course_id:
                self.created_courses.remove(course)
                print(f"Course {course.course_name} (ID: {course_id}) removed successfully.")
                return True

        print(f"Course with ID {course_id} not found or not created by you.")
        return False

    def update_course_info(self, course_id: str, new_name: str = None):
        for course in self.created_courses:
            if course.course_id == course_id:
                if new_name:
                    course.course_name = new_name
                    print(f"Course name updated to {new_name}")
                return True

        print(f"Course with ID {course_id} not found or not created by you.")
        return False


