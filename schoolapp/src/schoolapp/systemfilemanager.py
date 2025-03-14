import json
import os

from schoolapp.src.schoolapp.course import Course


class SystemFileManager:
    def _init_(self):
        self.students = []
        self.instructors = []
        self.courses = []



    # def save_data(self,filename:str):
    #     data = {
    #         "students": [{"email": s.email, "password": s._password, "name": s.name, "student_id": s.student_id} for s in
    #                      self.students],
    #         "instructors": [{"email": i.email, "password": i._password, "name": i.name, "instructor_id": i.instructor_id}
    #                         for i in self.instructors],
    #         "courses": [{"course_name": c.course_name, "course_id": c.course_id, "instructor_email": c.instructor.email}
    #                     for c in self.courses]
    #     }
    #     with open(filename, "w") as file:
    #         json.dump(data, file)

    def save_course(self,filename:str,key:str,values):
        data = {
            key : [{f"{key}_name": course_data.course_name, f"{key}_id": course_data.course_id, f"{key}_email": course_data.instructor }
                        for course_data in values]
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_course(self,filename:str,key:str, values:list):
        with open(filename, "r") as file:
            data = json.load(file)
            for course_data in data[key]:
                name = course_data.get("name")
                course_id = course_data.get("course_id")
                instructor = course_data.get("instructor")
                course = Course(name, course_id, instructor)
                values.append(course)
        return values





    # def load_data(self, filename:str):
    #     with open(filename, "r") as file:
    #         data = json.load(file)
    #         for s in data["students"]:
    #              self.students.append(Student(s["email"], s["password"], s["name"], s["student_id"]))
    #         for i in data["instructors"]:
    #                 self.instructors.append(Instructor(i["email"], i["password"], i["name"], i["instructor_id"]))
    #         for c in data["courses"]:
    #             instructor = next((i for i in self.instructors if i.email == c["instructor_email"]), None)
    #             if instructor:
    #                 course = instructor.create_course(c["course_name"], c["course_id"])
    #                 self.courses.append(course)


    def delete_data(self,filename:str):
        os.remove(filename)
        print("file deleted Successfully.")
