import unittest

from email_validator import EmailNotValidError

from schoolapp.exception.exceptions import UserAlreadyExist, InvalidLoginDetails, PasswordNotAccepted, \
    InvalidCourseDetails
from schoolapp.src.schoolapp import course
from schoolapp.src.schoolapp.instructor import Instructor
from schoolapp.src.schoolapp.student import Student
from schoolapp.src.schoolapp.systemfilemanager import SystemFileManager


class MyInstructor(unittest.TestCase):
    def setUp(self):
        self.student= Student("Student@gmail.com", "P@ssw0rd123","first_name","last_name")
        self.system_file = SystemFileManager()
    def tearDown(self):

        self.student = None

    def test_that_Student_can_register(self):
        self.assertEqual( "first_name", self.student.first_name)
        self.assertEqual( "last_name", self.student.last_name)
        self.assertEqual( f"S-0{Student.count - 1}", self.student.student_id)

    def test_that_student_cannot_register_with_invalid_password(self):
        with self.assertRaises(PasswordNotAccepted):
            self.student2 = Student("Student@gmail.com", "invalidpass", "first_name", "last_name")

    def test_that_student_cannot_register_with_invalid_email(self):
        with self.assertRaises(EmailNotValidError):
            self.student2 = Student("Studentinvalidemail", "P@ssw0rd123", "first_name", "last_name")

    def test_that_student_can_login(self):
        self.assertFalse(self.student.is_logged_in)
        self.student.login_user("Student@gmail.com", "P@ssw0rd123")
        self.assertTrue(self.student.is_logged_in)

    def test_that_student_can_logout(self):
        self.assertFalse(self.student.is_logged_in)
        self.student.login_user("Student@gmail.com", "P@ssw0rd123")
        self.assertTrue(self.student.is_logged_in)
        self.student.logout_user()
        self.assertFalse(self.student.is_logged_in)

    def test_that_student_can_view_created_courses_by_instructor_(self):
        self.instructor = Instructor("Instructor@email.com", "P@ssw0rd123", "first_name", "last_name")
        self.instructor.login_user("Instructor@email.com", "P@ssw0rd123")
        self.instructor.create_course("course_name","Code101" )
        self.student.login_user("Student@gmail.com", "P@ssw0rd123")
        courses = self.student.view_available_courses()[0]
        self.assertEqual(course.Course("course_name","Code101","first_name last_name" ) , courses  )
        self.system_file.delete_data('courses.json')

    def test_that_student_can_enroll_for_instructor_courses(self):
        self.instructor = Instructor("Instructor@email.com", "P@ssw0rd123", "first_name", "last_name")
        self.instructor.login_user("Instructor@email.com", "P@ssw0rd123")
        self.instructor.create_course("course_name2","Code101" )
        self.student.login_user("Student@gmail.com", "P@ssw0rd123")
        courses = self.student.view_available_courses()[0]
        self.assertEqual(course.Course("course_name","Code101","first_name last_name" ) , courses  )
        self.student.register_course("Code101")
        self.assertEqual(course.Course("course_name","Code101","first_name last_name" ), self.student.get_enrolled_course()[0])
        self.system_file.delete_data('courses.json')

    # def test_that_student_can_not_register_a_course_twice_(self):
    #     self.instructor = Instructor("Instructor@email.com", "P@ssw0rd123", "first_name", "last_name")
    #     self.instructor.login("Instructor@email.com", "P@ssw0rd123")
    #     self.instructor.create_course("course_name2", "Code101")
    #     self.student.login("Student@gmail.com", "P@ssw0rd123")
    #     courses = self.student.view_available_courses()[0]
    #     self.assertEqual(course.Course("course_name", "Code101", "first_name last_name"), courses)
    #     self.student.register_course("Code101")
    #     self.assertEqual(course.Course("course_name", "Code101", "first_name last_name"),self.student.get_enrolled_course()[0])
    #     with self.assertRaises(InvalidCourseDetails):
    #         self.student.register_course("Code101")
    #     self.system_file.delete_data('courses.json')

    def test_that_student_can_view_grades_of_a_course(self):
        self.instructor = Instructor("Instructor@email.com", "P@ssw0rd123", "first_name", "last_name")
        self.instructor.login_user("Instructor@email.com", "P@ssw0rd123")
        self.instructor.create_course("course_name2", "course_id")
        self.student.login_user("Student@gmail.com", "P@ssw0rd123")
        courses = self.student.view_available_courses()[0]
        self.assertEqual(course.Course("course_name", "course_id", "first_name last_name"), courses)
        self.student.register_course("course_id")
        self.assertEqual(course.Course("course_name", "course_id", "first_name last_name"),self.student.get_enrolled_course()[0])
        self.instructor.view_students_in_course('course_id')
        self.instructor.assign_grades('course_id', 'student_name', 'grade')

        self.system_file.delete_data('instructor.json')
        self.system_file.delete_data('courses.json')





   
