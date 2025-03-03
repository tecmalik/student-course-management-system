import unittest

from schoolapp.src.schoolapp.student import Student


class MyTestCase(unittest.TestCase):
    def  setUp(self) -> None:
        self.student = Student("name","email","password","S-101")
    def test_student_can_register_with_valid_details(self):
        pass





if __name__ == '__main__':
    unittest.main()
