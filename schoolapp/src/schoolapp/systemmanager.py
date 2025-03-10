class SystemManager:
    def _init_(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def save_data(self, filename="data.json"):
        data = {
            "students": [{"email": s.email, "password": s.password, "name": s.name, "student_id": s.student_id} for s in
                         self.students],
            "instructors": [{"email": i.email, "password": i.password, "name": i.name, "instructor_id": i.instructor_id}
                            for i in self.instructors],
            "courses": [{"course_name": c.course_name, "course_id": c.course_id, "instructor_email": c.instructor.email}
                        for c in self.courses]
        }
