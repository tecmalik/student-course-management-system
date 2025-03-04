import unittest
from schoolapp.src.schoolapp.instructor import Instructor
from schoolapp.src.schoolapp.student import Student


class MyInstructor(unittest.TestCase):
    def setUp(self):
        # self.instructor = Instructor("name","email@email.com", "Password")
        ...
    def test_that_instructor_can_register(self):
        instructor = Instructor("name", "email@email.com", "Password")
        self.assertEqual( "name", instructor._name())
















if __name__ == '__main__':
    unittest.main()
