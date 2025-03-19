import json
import os

from schoolapp.src.schoolapp.course import Course


class SystemFileManager:
    def _init_(self):
        self.students = []
        self.instructors = []
        self.courses = []



    def save_course(self,filename:str,key:str,values):
        data = {
            key : [{f"{key}_name": course_data.course_name, f"{key}_id": course_data.course_id, f"{key}_instructor": course_data.instructor }
                        for course_data in values]
        }
        with open(filename, "w") as file:
            json.dump(data, file)


    #     try:
        #     with open(filename, "w") as file:
        #         json.dump(data, file)
        # except (IOError, json.JSONEncoder.encode) as e:  # Catch potential errors
        #     print(f"Error saving course data to {filename}: {e}")

    def load_course(self, filename: str, key: str, values: list):
        with open(filename, "r") as file:
            data = json.load(file)
            course_data = data[key]
            for course in course_data:
                course_name = course[f'{key}_name']
                course_id = course[f'{key}_id']
                course_instructor = course[f'{key}_instructor']
                course = Course(course_name, course_id, course_instructor)
                values.append(course)
        return values


    def delete_data(self,filename:str):
        os.remove(filename)
        print("file deleted Successfully.")



    def save_student(self, filename:str, key:str , value):
        data = {
            key: {'student_name': value[0], 'student_id': value[1], 'student_grade': "no grade assigned"}
        }
        with open(filename, "w") as outfile:
            json.dump(data, outfile)

    def load_enrolled_student(self, filename:str, key:str, value ):
        with open(filename , "r") as file:
            data = json.load(file)
            course_data = data[key]
            value.append(course_data)
        return value
