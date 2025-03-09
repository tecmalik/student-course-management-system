<<<<<<< HEAD
class User:
    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_logged_in = False

    def register(self, first_name: str, last_name: str, email: str, password: str):
        return User(first_name, last_name, email, password)

    def login(self, email: str, password: str):
        if self.email == email and self.password == password:
            self.is_logged_in = True
            return "Login successful"
        else:
            return "Invalid email or password"

    def logout(self):
        if self.is_logged_in:
            self.is_logged_in = False
            return "Logout successful"
        else:
            return "User is already logged out"

=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
import re

EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PASSWORD_PATTERN = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
STUDENT_ID_PATTERN = r'^[a-z]$'
INSTRUCTOR_ID_PATTERN = r'^I\d{3}$'


>>>>>>> 23fba7d2f44df48f88259e8b16866a8dc20bd928
class User:
    def _init_(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self,name, email, password):
            if not re.match(EMAIL_PATTERN, email):
                raise ValueError("Invalid email format.")
            if not re.match(PASSWORD_PATTERN, password):
<<<<<<< HEAD
                raise ValueError("Password must be at least 8 characters with one letter and one number.")
            self.email = email
            self.password = password
            self.name = name
            return True
=======

                raise ValueError("Password must be at least 8
>>>>>>> 23fba7d2f44df48f88259e8b16866a8dc20bd928
>>>>>>> ed7fab485545253c70cb82f9589e01caf4c15d92
>>>>>>> 90f73b6110bedf48b1619a431d4b86c34b8ef31a
