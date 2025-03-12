import unittest

from schoolapp.src.schoolapp import course

class Mycourse(unittest.TestCase):
    def setUp(self):
        self.course = course.course()
        ...
    def test_that_course_can_be_created(self):
        self.assertEqual( "name", self.course.name)
    # def test_that_a_course_can_be_created(self):
    #     self.course.create_course("course_name", "course_code", "course_level","instructors_name")
    #     self.assertEqual( "course_name", self.course.course_name)
    # def test_that_course_willThat_exception_for_invalid_course_code(self):
    #     pass
