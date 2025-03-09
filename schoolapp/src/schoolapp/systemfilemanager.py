import json
import os
class SystemManager:
    def _init_(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def save_data(self,filename:str):
        data = {
            "students": [{"email": s.email, "password": s.password, "name": s.name, "student_id": s.student_id} for s in
                         self.students],
            "instructors": [{"email": i.email, "password": i.password, "name": i.name, "instructor_id": i.instructor_id}
                            for i in self.instructors],
            "courses": [{"course_name": c.course_name, "course_id": c.course_id, "instructor_email": c.instructor.email}
                        for c in self.courses]
        }
        with open(filename, "w") as file:
            json.dump(data, file)


    def load_data(self, filename:str):
        with open(filename, "r") as file:
            data = json.load(file)
            for s in data["students"]:
                 self.students.append(Student(s["email"], s["password"], s["name"], s["student_id"]))
            for i in data["instructors"]:
                    self.instructors.append(Instructor(i["email"], i["password"], i["name"], i["instructor_id"]))
            for c in data["courses"]:
                instructor = next((i for i in self.instructors if i.email == c["instructor_email"]), None)
                if instructor:
                    course = instructor.create_course(c["course_name"], c["course_id"])
                    self.courses.append(course)

        os.remove(filename)
        print("file deleted Successfully.")


