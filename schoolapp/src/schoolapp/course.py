from schoolapp.exception.exceptions import InvalidArgumentException
from schoolapp.src.schoolapp.user import User


class Course:
    def _init_(self, course_name, course_id, instructor):
        self._course_name = course_name
        self._course_id = course_id
        self._instructor = instructor
        self._enrolled_students = []

    @property
    def course_name(self):
        return self._course_name
    @property
    def course_id(self):
        return self._course_id
    @property
    def instructor(self):
        return self._instructor

    @course_id.setter
    def course_id(self, course_id):
        if course_id is None:
            raise InvalidArgumentException("course_name cannot be None")
        if course_id.strip() == "":
            raise InvalidArgumentException("course_name cannot be empty")
        self._course_id = course_id

    @course_name.setter
    def course_name(self, course_name):
        if course_name is None:
            raise InvalidArgumentException("course_name cannot be None")
        if course_name.strip() == "":
            raise InvalidArgumentException("course_name cannot be empty")
        self._course_name = course_name

    @instructor.setter
    def instructor(self, instructor):
        if instructor is None:
            raise InvalidArgumentException("course_name cannot be None")
        if instructor.strip() == "":
            raise InvalidArgumentException("course_name cannot be empty")
        self._instructor = instructor

    def add_student(self, student):
        self._enrolled_students.append(student)

    def remove_student(self, student):
        for student in self._enrolled_students:
            if student.student_id == student.student_id:
                self._enrolled_students.remove(student)

    def number_of_student(self):
        return len(self._enrolled_students)

    def _eq_(self, other,):
        if isinstance(other,Course):
            return self.course_id ==other.course_id