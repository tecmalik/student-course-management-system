<<<<<<< HEAD
class Instructor:
    def __init__(self, email, password, name, instructor_id):
        self.email = email
        self.password = password
        self.name = name
        self.instructor_id = instructor_id
        self.created_courses = []
        self.students_in_courses = {}

    def create_course(self, course_name, course_id):
        course = {"name": course_name, "id": course_id}
        self.created_courses.append(course)
        self.students_in_courses[course_id] = []
        print(f"Course '{course_name}' created successfully!")

    def delete_course(self, course_name, course_id):
        self.created_courses = [course for course in self.created_courses if not (course["name"] == course_name and course["id"] == course_id)]
        if course_id in self.students_in_courses:
            del self.students_in_courses[course_id]
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





=======
<<<<<<< HEAD
=======

import re
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

>>>>>>> ed7fab485545253c70cb82f9589e01caf4c15d92
>>>>>>> 90f73b6110bedf48b1619a431d4b86c34b8ef31a
