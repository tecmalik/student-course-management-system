<<<<<<< HEAD
class Course:
    def __init__(self, course_name, course_id, instructor):
=======
class course:
    def __init__(self,course_name, course_id, instructor):
>>>>>>> 90f73b6110bedf48b1619a431d4b86c34b8ef31a
        self.course_name = course_name
        self.course_id = course_id
        self.instructor = instructor
        self.enrolled_students = []
<<<<<<< HEAD
        self.grades = []

    def add_student(self, student):
        if student in self.enrolled_students:
            raise ValueError("Student already enrolled.")
        self.enrolled_students.remove(student)

=======
        self.grades = {}


    def get_grade(self, student):
        return self.grades[student.student_id]

    def set_grade(self, student, grade):
        self.grades[student.student_id] = grade

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            if student.student_id in self.grades:
                self.grades.pop(student.student_id)

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def get_enrolled_students(self):
        return self.enrolled_students
>>>>>>> 90f73b6110bedf48b1619a431d4b86c34b8ef31a
