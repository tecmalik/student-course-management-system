import re


class Student(User):
    def __init__(self, email, password, name):
        super().__init__(email, password)
        self.student_id = f"S{uuid.uuid4().hex[:3]}"
        self.enrolled_courses = []

    def view_available_courses(self, courses):
        return [course.course_name for course in courses]

    def view_register_courses(self,course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.enrolled_student.append(self)
            print(f"{student_id}, You have enroll for {course.course_name}")



