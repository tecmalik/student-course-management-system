import unittest

from schoolapp.exception.exceptions import InvalidArgumentException
from schoolapp.src.schoolapp import course
from schoolapp.src.schoolapp.student import Student


class MyCourse(unittest.TestCase):
    def setUp(self):
        self.course = course.Course('course_name', 'course_id', 'instructor')

    def test_that_course_created_has_a_name(self):
        self.assertEqual( "course_name", self.course.course_name)
    def test_that_course_will_raise_exception_for_an_empty_or_invalid_course_name(self):
        with self.assertRaises(InvalidArgumentException):
            self.course.course_name=" "
    def test_that_course_code_can_not_be_empty(self):
        with self.assertRaises(InvalidArgumentException):
            self.course.course_id=""
    def test_that_course_has_a_course_code(self):
        self.assertEqual(self.course.course_id,'course_id',)
    def test_that_course_can_have_student_enrolled(self):
        self.course.add_student(Student("Student@gmail.com", "P@ssw0rd123", "first_name", "last_name"))
        self.assertEqual(1,self.course.number_of_student())
    def test_that_course_can_remove_students_of_enrolled_students(self):
        self.course.remove_student(Student("Student@gmail.com", "P@ssw0rd123","first_name", "last_name"))
        self.assertEqual(0,self.course.number_of_student()),

