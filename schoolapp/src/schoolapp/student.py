class Student:
    def __init__(self, email, password, name, student_id):
        self.email = email
        self.password = password
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def view_available_courses(self, courses):
        print("Available Courses:")
        for course in courses:
            print(course)

    def register_course_and_instructor(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"Registered for course: {course}")
        else:
            print(f"Already enrolled in {course}")

    def view_registered_courses(self):
        print("Registered Courses:")
        if self.enrolled_courses:
            for course in self.enrolled_courses:
                print(course)
        else:
            print("No courses registered.")

    def view_grade(self):
        print("Grades are not yet implemented.")

    def unregister_a_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print(f"Unregistered from course: {course}")
        else:
            print(f"Not enrolled in {course}")

