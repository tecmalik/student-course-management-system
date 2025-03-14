import json
import os
from schoolapp.src.schoolapp.course import Course
from schoolapp.src.schoolapp.bcrypt import Bcrypt


class SystemFileManager:
    def __init__(self):
        self.data_directory = "data"
        self.bcrypt = Bcrypt()
        os.makedirs(self.data_directory, exist_ok=True)

    def _get_filepath(self, filename):
        return os.path.join(self.data_directory, filename)


    def save_courses(self, filename, courses):

        filepath = self._get_filepath(filename)
        data = []

        for course in courses:
            course_data = {
                "course_name": course.course_name,
                "course_id": course.course_id,
                "instructor": course.instructor,
                "enrolled_students": [student.student_id for student in course._enrolled_students] if hasattr(course,'_enrolled_students') else []

            }
            data.append(course_data)

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        return True

    def load_courses(self, filename):
        filepath = self._get_filepath(filename)
        courses = []

        try:
            with open(filepath, "r") as file:
                data = json.load(file)

                for course_data in data:
                    course = Course(
                        course_data["course_name"],
                        course_data["course_id"],
                        course_data["instructor"]
                    )
                    courses.append(course)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        return courses


    def save_students(self, filename, students):
        filepath = self._get_filepath(filename)
        data = []

        for student in students:
            password_str = student._password.decode('utf-8') if isinstance(student._password, bytes) else str(
                student._password)

            student_data = {
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student._email,
                "password": password_str,
                "student_id": student.student_id,
                "enrolled_courses": [course.course_id for course in student.enrolled_courses] if hasattr(student,'enrolled_courses') else []

            }
            data.append(student_data)

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        return True

    def load_students(self, filename, student_class):
        filepath = self._get_filepath(filename)
        students = []

        try:
            with open(filepath, "r") as file:
                data = json.load(file)

                for student_data in data:

                    student = student_class(
                        student_data["email"],
                        "",
                        student_data["first_name"],
                        student_data["last_name"]
                    )

                    student.student_id = student_data["student_id"]
                    student._password = student_data["password"].encode('utf-8') if isinstance(student_data["password"],str) else student_data["password"]


                    student.enrolled_courses = []

                    students.append(student)
        except (FileNotFoundError, json.JSONDecodeError):

            pass

        return students


    def save_instructors(self, filename, instructors):
        filepath = self._get_filepath(filename)
        data = []

        for instructor in instructors:

            password_str = instructor._password.decode('utf-8') if isinstance(instructor._password, bytes) else str(
                instructor._password)

            instructor_data = {
                "first_name": instructor.first_name,
                "last_name": instructor.last_name,
                "email": instructor._email,
                "password": password_str,
                "instructor_id": instructor.instructor_id,

                "created_courses": [course.course_id for course in instructor.created_courses] if hasattr(instructor,
                                                                                                          'created_courses') else []
            }
            data.append(instructor_data)

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        return True

    def load_instructors(self, filename, instructor_class):

        filepath = self._get_filepath(filename)
        instructors = []

        try:
            with open(filepath, "r") as file:
                data = json.load(file)

                for instructor_data in data:

                    instructor = instructor_class(
                        instructor_data["email"],
                        "",
                        instructor_data["first_name"],
                        instructor_data["last_name"]
                    )

                    instructor.instructor_id = instructor_data["instructor_id"]
                    instructor._password = instructor_data["password"].encode('utf-8') if isinstance(
                        instructor_data["password"], str) else instructor_data["password"]
                    instructor.created_courses = []

                    instructors.append(instructor)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        return instructors


    def link_data(self, students, instructors, courses):


        courses_dict = {course.course_id: course for course in courses}
        students_dict = {student.student_id: student for student in students}
        instructors_dict = {instructor.instructor_id: instructor for instructor in instructors}


        filepath_instructors = self._get_filepath("instructors.json")
        try:
            with open(filepath_instructors, "r") as file:
                instructors_data = json.load(file)

                for instructor_data in instructors_data:
                    instructor_id = instructor_data["instructor_id"]
                    if instructor_id in instructors_dict:
                        instructor = instructors_dict[instructor_id]

                        for course_id in instructor_data["created_courses"]:
                            if course_id in courses_dict:
                                instructor.created_courses.append(courses_dict[course_id])
        except (FileNotFoundError, json.JSONDecodeError):
            pass


        filepath_students = self._get_filepath("students.json")
        try:
            with open(filepath_students, "r") as file:
                students_data = json.load(file)

                for student_data in students_data:
                    student_id = student_data["student_id"]
                    if student_id in students_dict:
                        student = students_dict[student_id]

                        for course_id in student_data["enrolled_courses"]:
                            if course_id in courses_dict:
                                student.enrolled_courses.append(courses_dict[course_id])
                                if student not in courses_dict[course_id]._enrolled_students:
                                    courses_dict[course_id]._enrolled_students.append(student)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        return students, instructors, courses


    def save_all_data(self, students, instructors, courses):
        self.save_students("students.json", students)
        self.save_instructors("instructors.json", instructors)
        self.save_courses("courses.json", courses)

        return True

    def load_all_data(self, student_class, instructor_class):
        students = self.load_students("students.json", student_class)
        instructors = self.load_instructors("instructors.json", instructor_class)
        courses = self.load_courses("courses.json")
        students, instructors, courses = self.link_data(students, instructors, courses)

        return students, instructors, courses