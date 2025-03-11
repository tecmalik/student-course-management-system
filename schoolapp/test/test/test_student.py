import unittest

from schoolapp.src.schoolapp.student import Student


class MyInstructor(unittest.TestCase):
    def setUp(self):
        self.student= Student("Student@gmail.com", "P@ssw0rd123","first_name","last_name")

    def tearDown(self):
        self.student = None

    def test_that_Student_can_register(self):
        self.assertEqual( "first_name", self.student.first_name)
        self.assertEqual( "last_name", self.student.last_name)
        self.assertEqual( f"S-0{Student.count - 1}", self.student.student_id)
