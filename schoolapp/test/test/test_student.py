import unittest

from schoolapp.src.schoolapp import student


class MyStudentTestCase(unittest.TestCase):
    def  setUp(self) -> None:
        self.student = student.Student("StudentName","studentemail@gmail.com","password","S-101")
    def test_student_can_register_with_valid_details(self):
        self.assertEqual("StudentName",self.student.name)
    def test_that_student_registered_has_an_id(self):
        self.assertEqual("S-101",self.student.student_id)
    def test_that_student_can_view_courses_(self):
        self.student2.Student("StudentName2", "studentemail2@gmail.com", "password2", "S-102")

        self.assertEqual("StudentName",self.student.name)
















if __name__ == '__main__':
    unittest.main()
