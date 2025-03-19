from schoolapp.exception.exceptions import CourseAlreadyExist, CourseDoesNotExist, InvalidLoginException
from schoolapp.src.schoolapp.course import Course
from schoolapp.src.schoolapp.user import User
from schoolapp.src.schoolapp.systemfilemanager import SystemFileManager



class Instructor(User):
    system_file = SystemFileManager()
    def __init__(self, email:str,  password:str, first_name: str, last_name: str):

        super().__init__(first_name, last_name, email, password)
        self.instructor_id = self.instructor_id()
        self.created_courses = []
        self.students_in_courses = {}
        Instructor.count += 1

    count = 1
    @staticmethod
    def instructor_id():
        return f"I-0{Instructor.count}"

    @property
    def get_instructor_id(self):
        return self.instructor_id

    def get_number_of_created_courses(self):
        return len(self.created_courses)

    def create_course(self, course_name, course_id):
        if self.is_logged_in == False:
            raise InvalidLoginException("user is not logged in")
        for course in self.created_courses:
            if course.course_name == course_name and course.course_id == course_id:
                raise CourseAlreadyExist(f'{course_name} already exists')
        course = Course( course_name,course_id , Instructor.get_fullname(self))
        self.created_courses.append(course)
        self.students_in_courses[course_id] = []
        print(f"Course '{course_name}' created successfully!")
        self.system_file.save_course('courses.json',"course",self.created_courses)

    def delete_course(self, course_name, course_id):
        if self.is_logged_in == False:
            raise InvalidLoginException("user is not logged in")
        if len(self.created_courses) == 0 :
            raise CourseDoesNotExist(f"{course_name} doesn't exist")
        for course in self.created_courses:
            if course.course_name == course_name and course.course_id == course_id:
                self.created_courses.remove(course)
        print(f"Course '{course_name}' deleted successfully!")

    def view_students_in_course(self, course_id):
        if self.is_logged_in == False:
            raise InvalidLoginException("user is not logged in")
        if self.created_courses == 0 :
            raise Exception(" no course has been created yet for student to enroll ")
        values  = []
        self.students_in_courses[course_id] = self.system_file.load_enrolled_student( 'instructor.json', course_id, values)
        students = self.students_in_courses[course_id]
        if len(students) == 0:
            raise Exception("No students enrolled yet")
        for student in students:
            print(f' Student name : {student['student_grade']} ID : {student['student_id']} grade : {student['student_grade']}')
        print(f"Students in course ID {course_id}: {students if students else 'No students enrolled yet.'}")


    def assign_grades(self, course_id, student_name, grade):
        if grade.isdigit() == False :
            raise Exception(" grade has to be digit")
        if int(grade) <=0 or int(grade) >= 100 :
            raise Exception(' grade not valid')
        if course_id.isspace() :
            raise Exception('course cannot be empty cant be empty')
        if student_name.isspace() :
            raise Exception('student name can not be empty cant be empty')
        if grade.isspace():
            raise Exception('grade can not be empty')

        if self.is_logged_in == False:
            raise InvalidLoginException("user is not logged in")

        if course_id not in self.students_in_courses:
            raise Exception(f"{course_id} not found")
        count = 0
        for student_info in self.students_in_courses[course_id]:
            print(student_info)
            if student_info["student_name"] == student_name:
                count += 1
        if count == 0:
            raise Exception(" Student has not enrolled")
        if student_name not in self.students_in_courses[course_id]:
                print(f"Student '{student_name}' not found in course ID {course_id}.")
                raise Exception(f"Student '{student_name}' doesn't exist")
        print(f"No such course with ID {course_id} exists.")
        for dict in self.students_in_courses[course_id]:
            if dict[course_id] == course_id and dict[student_name] == student_name:
                dict['student_grade'] = grade
        self.system_file.save_graded_students('graded_student.json',self.students_in_courses[course_id])



    def view_created_courses(self):
        if self.is_logged_in == False:
            raise InvalidLoginException("user is not logged in")
        print("Created courses:")
        for course in self.created_courses:
            print(f"Course Name: {course['name']}, Course ID: {course['id']}")
        if not self.created_courses:
            print("No courses created yet.")

    def view_students_and_grades(self, course_id):
        if self.is_logged_in == False:
            raise InvalidLoginException("user is not logged in")
        if course_id in self.students_in_courses:
            print(f"Students and grades for course ID {course_id}:")
            for student in self.students_in_courses[course_id]:
                print(f"- {student}: [Grade Not Implemented Yet]")
        else:
            print(f"No such course with ID {course_id} exists.")


    def view_all_grades(self):
        pass

