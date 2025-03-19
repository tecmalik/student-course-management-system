import unittest

from schoolapp.exception.exceptions import UserAlreadyExist, InstructorAlreadyRegistered
from schoolapp.src.schoolapp.instructors import Instructors


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.instructors = Instructors()

    def tearDown(self):
        self.instructors = None

    def test_that_instructor_can_register(self):
        self.instructors.register("malik","ojo","abdumalik@gmail.com","Passw0rd123")
        self.assertEqual(1, self.instructors.get_instructors_size())

    def test_that_i_can_register_multiple_instructors(self):
        self.instructors.register("matin","ojo","mali@gmail.com",'Matin123')
        self.instructors.register("malik", "ojo", "abdumalik@gmail.com", "Passw0rd123")
        self.assertEqual(2, self.instructors.get_instructors_size())

    def test_that_i_can_find_an_instructor_in_the_list_of_instructors(self):
        self.instructors.register("matin", "ojo", "mali@gmail.com", 'Matin123')
        self.instructors.register("malik", "ojo", "abdumalik@gmail.com", "Passw0rd123")
        self.assertEqual(2, self.instructors.get_instructors_size())
        instructor = self.instructors.find_by_email("abdumalik@gmail.com")
        self.assertEqual("abdumalik@gmail.com",instructor.get_email)

    def test_that_duplicate_instructor_cannot_be_registered(self):
        self.instructors.register("matin", "ojo", "mali@gmail.com", 'Matin123')
        self.instructors.register("malik", "ojo", "abdumalik@gmail.com", "Passw0rd123")
        self.assertEqual(2, self.instructors.get_instructors_size())
        with self.assertRaises(InstructorAlreadyRegistered):
            self.instructors.register("matin", "ojo", "mali@gmail.com", 'Matin123')
        self.assertEqual(2, self.instructors.get_instructors_size())

    def test_that_i_can_find_an_instructor_by_email(self):
        self.instructors.register("matin", "ojo", "mali@gmail.com", 'Matin123')
        self.instructors.register("malik", "ojo", "abdumalik@gmail.com", "Passw0rd123")
        self.assertEqual(2, self.instructors.get_instructors_size())


if __name__ == '__main__':
    unittest.main()
