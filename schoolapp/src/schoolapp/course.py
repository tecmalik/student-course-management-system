from schoolapp.src.schoolapp import instructor


class Course :
    def _init_(self, course_name, course_code,course_grade):
        self._course_name = course_name
        self._course_code = course_code
        self.student = []
        self._instructor = instructor.Instructor("name", "password@gmail.com", "password")


    @property
    def course_name(self):
        return self._course_name
    @property
    def course_code(self):
        return self._course_code

    @course_name.setter
    def course_name(self, course_name):
        self._course_name = course_name

    @course_code.setter
    def course_code(self, course_code):
        self._course_code = course_code

    @property
    def course_grade(self):
        return self._course_grade
    @course_grade.setter
    def course_grade(self, course_grade):
        self._course_grade = course_grade

    def get_instructor(self):
        return self._instructor.name



