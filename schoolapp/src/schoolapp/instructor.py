import re

from CourseManagement.Courses import Course
from User import User, INSTRUCTOR_ID_PATTERN


class Instructor(User):
    def _init_(self, email, password, name, instructor_id):
        super()._init_(email, password, name)
        if not re.match(INSTRUCTOR_ID_PATTERN, instructor_id):
            raise ValueError("Invalid instructor ID format.")
        self.instructor_id = instructor_id
        self.created_courses = []

    def create_course(self, course_name, course_id):
        course = Course(course_name, course_id, self)
        self.created_courses.append(course)
        return course

