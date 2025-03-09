
class Course:
    def __init__(self, course_name, course_id, instructor):
        self.course_name = course_name
        self.course_id = course_id
        self.instructor = instructor
        self.enrolled_students = []
        self.grades = []

    def add_student(self, student):
        if student in self.enrolled_students:
            raise ValueError("Student already enrolled.")
        self.enrolled_students.remove(student)


