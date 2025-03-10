<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
import re

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PASSWORD_PATTERN = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
STUDENT_ID_PATTERN = r'^[a-z]$'
INSTRUCTOR_ID_PATTERN = r'^I\d{3}$'

class User:
    def _init_(self, first_name, last_name, email , password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.isLoggedIn = False

    def register(self,name, email, password):
            if not re.match(EMAIL_PATTERN, email):
                raise ValueError("Invalid email format.")
            if not re.match(PASSWORD_PATTERN, password):
                raise ValueError("Password must be at least 8 characters with one letter and one number.")
            self.email = email
            self.password = password
            self.name = name
            return True