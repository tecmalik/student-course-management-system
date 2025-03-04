from sympy.physics.units.definitions.unit_definitions import statC


class Course :
    def __init__(self, course_name, course_code, course_level,instructors_name):
        self.validate_course_code(course_code)
        self._course_name = course_name
        self._course_code =  course_code
        self._course_level = course_level
        self._instructor_name = instructors_name
        self.student = []


    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, course_name):
        self._course_name = course_name

    @property
    def course_code(self):
        return self._course_code

    @course_code.setter
    def course_code(self, course_code):
        self._course_code = course_code
    @staticmethod
    def validate_course_code(course_code:str):
        if not course_code :
            raise ValueError("course_code cannot be empty")
        if not course_code.isalnum():
            raise ValueError("course_code must be alphanumeric")
        if len(course_code) != 6 :
            raise ValueError("course_code must be 6 characters")

