import unittest
from schoolapp.src.schoolapp.instructor import Instructor


class MyInstructor(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor("name","email@email.com", "Password")
        ...
    def test_that_instructor_can_register(self):
        self.assertEqual( "name", self.instructor.name)
    def test_that_instructor_can_create_a_course(self):
        self.instructor.create_course("English", 'course_name', 'course_level', 'instructor_name')
        self.assertEqual( 1, self.instructor.get_number_of_created_courses())
    def test_that_instructor_can_view_list_of__enrolled_students(self):
        passs

















if __name__ == '__main__':
    unittest.main()
