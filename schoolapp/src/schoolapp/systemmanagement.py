import json

from schoolapp.src.schoolapp.student import Student
from schoolapp.src.schoolapp.instructor import Instructor


class SystemManagement:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def save_data(self,filename = "data.json"):
        data = {
            "Students" : [{"email":s.email, "password":s.password,"name": s.name,"student_id": s.student_id} for s in self.students ],
            "instructors" : [{"email": i.email,"password":i.password, "name":i.name,"instructor_id": i.instructor_id} for i in self.instructors ],
            "courses":[{'courses_name':c.courses_name,"course_id":c.course_id,"instructor_email":c.instructor.email} for c in self.courses ]
        }
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def load_data(self, filename="data.json"):
        with open(filename, 'r') as infile:
            data = json.load(infile)
            for s in data["students"]:
                self.students.append(Student(s["email"],s["password"],s["name"],s["instructor_email"]),None)
            for i in data["instructors"]:
                self.instructors.append(Instructor(i["email"],i["password"],i["name"],i["instructor_id"]))
            for c in data["courses"]:
                instructor = next((i for i in self.instructors if i.email == c["instructor_email"]), None)
                if instructor:
                    course = instructor.create_course(c["courses_name"],c["course_id"],c["instructor_email"])
                    self.courses.append(course)


