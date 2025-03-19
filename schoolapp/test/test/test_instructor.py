import unittest

from email_validator import EmailNotValidError
from schoolapp.exception.exceptions import PasswordNotAccepted, PasswordTooShort, CourseAlreadyExist, \
    CourseDoesNotExist, InvalidLoginException, UserAlreadyExist
from schoolapp.src.schoolapp.instructor import Instructor
from schoolapp.src.schoolapp.student import Student
from schoolapp.src.schoolapp.systemfilemanager import SystemFileManager

class MyInstructor(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor("first_name","last_name","Instructor@email.com", "Passw0rd123")

    def test_that_instructor_can_login(self):
        self.assertFalse(self.instructor.is_logged_in)
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        self.assertTrue(self.instructor.is_logged_in)

    def test_that_instructor_can_be_log_out(self):
        self.assertFalse(self.instructor.is_logged_in)
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        self.assertTrue(self.instructor.is_logged_in)
        self.instructor.logout_user()
        self.assertFalse(self.instructor.is_logged_in)

    def test_that_instructor_can_register(self):
        self.assertEqual( "first_name", self.instructor.first_name)
        self.assertEqual( "last_name", self.instructor.last_name)
        self.assertEqual( f"I-0{Instructor.count - 1}", self.instructor.get_instructor_id)

    def test_that_instructor_can_create_a_course(self):
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        self.instructor.create_course("course_name","Code101" )
        self.assertEqual( 1, self.instructor.get_number_of_created_courses())

    def test_that_instructor_cannot_create_a_course_when_logged_out(self):
        self.assertFalse(self.instructor.is_logged_in)
        with self.assertRaises(InvalidLoginException) :
            self.instructor.create_course("course_name","Code101" )
        self.assertEqual( 0, self.instructor.get_number_of_created_courses())

    def test_that_instructor_can_not_create_duplicate_courses(self):
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        self.instructor.create_course("course_name","Code101" )
        self.assertEqual( 1, self.instructor.get_number_of_created_courses())
        with self.assertRaises(CourseAlreadyExist):
            self.instructor.create_course("course_name","Code101" )
        self.assertEqual( 1, self.instructor.get_number_of_created_courses())
        self.system_file = SystemFileManager()
        self.system_file.delete_data('courses.json')

    def test_that_instructor_can_not_register_With_invalid_password(self):
        self.instructor.login_user("Instructor@email.com", "Pssw0rd123")
        with self.assertRaises(PasswordNotAccepted) :
            Instructor( "Instructor@email.com", "password","first_name","last_name")
        with self.assertRaises(PasswordTooShort) :
            Instructor( "Instructor@email.com", "pssw","first_name","last_name")

    def test_that_instructor_can_not_register_with_invalid_email(self):
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        with self.assertRaises(EmailNotValidError) :
            Instructor( "first_name","last_name","Instructor", "Password123")
        with self.assertRaises(EmailNotValidError) :
            Instructor( "first_name","last_name","Instructor", "Password123")

    def test_that_instructor_can_delete_created_courses(self):
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        self.instructor.create_course("course_name","Code101" )
        self.assertEqual( 1, self.instructor.get_number_of_created_courses())
        self.instructor.delete_course("course_name","Code101")
        self.assertEqual( 0, self.instructor.get_number_of_created_courses())

    def test_that_instructor_can_not_delete_a_course_that_does_not_exist(self):
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        with self.assertRaises(CourseDoesNotExist):
            self.instructor.delete_course("course_name","Code101")

    def test_that_instructor_can_view_list_of_enrolled_student(self):
        self.instructor.login_user("Instructor@email.com", "Passw0rd123")
        self.instructor.create_course("course_name", "Code101")
        self.assertEqual(1, self.instructor.get_number_of_created_courses())
        self.student = Student("Student@gmail.com", "Passw0rd123", "first_name", "last_name")
        self.student.login_user("Student@gmail.com", "Passw0rd123")
        self.student.register_course("Code101")



        







if __name__ == '__main__':
    unittest.main()
