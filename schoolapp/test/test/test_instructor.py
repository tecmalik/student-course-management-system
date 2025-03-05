import unittest

from mako.testing.assertions import assert_raises_message_with_proper_context

from schoolapp.src.schoolapp.instructor import Instructor


class MyInstructor(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor("name","email@email.com", "Password","I-101")
    def test_that_instructor_can_register(self):
        self.assertEqual( "name", self.instructor.name)
    def test_that_instructor_can_create_a_course(self):
        self.instructor.create_course('course_name','Eng101' , 'course_level', 'instructor_name')
        self.assertEqual( 1, self.instructor.get_number_of_created_courses())
    def test_that_instructor_can_raise_error_for_invalid_code_create_a_course(self):
        with self.assertRaises(ValueError) :self.instructor.create_course('course_name','code101' , 'course_level', 'instructor_name')
    def test_that_instructor_can_throw_error_create_invalid_course(self):
        with self.assertRaises(Exception):self.instructor.create_course("English", 'course_name', 'course_level', 'instructor_name')
    def test_that_instructor_can_not_register_with_same_email(self):
        self.instructor.register("email@email.com", "password2")
        with self.assertRaises(Exception): self.instructor.register("email@email.com","password")
    def test_that_instructor_can_view_list_of_enrolled_courses(self):
        self.instructor.register("email@email.com", "password")
        self.assertEqual("james",self.instructor.view_enrolled_student()[1])


















if __name__ == '__main__':
    unittest.main()
