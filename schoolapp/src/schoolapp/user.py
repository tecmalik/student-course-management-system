from abc import ABC, abstractmethod

from schoolapp.src.schoolapp import bcrypt
from schoolapp.src.schoolapp.bcrypt import Bcrypt
from schoolapp.src.schoolapp.validator import Validator
from schoolapp.exception.exceptions import InvalidLoginException


class User(ABC):
    validator = Validator()
    bcrypt = Bcrypt()
    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.validator.validate_name (first_name, last_name)
        self.validator.validate_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self._email =  self.validator.validate_email(email)
        self._password = self.bcrypt.encrypt_password(password)
        self._is_logged_in = False

    @property
    def is_logged_in(self):
        return self._is_logged_in

    @is_logged_in.setter
    def is_logged_in(self, value):
        self._is_logged_in = value

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._lastname

    @last_name.setter
    def last_name(self, value):
        self._lastname = value

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def login(self, email: str, password:str):
        if email == self._email and  bcrypt.Bcrypt.check_password(self,password, self._password):
            self._is_logged_in = True
            return "Login successful"
        raise InvalidLoginException("Invalid email or password")

    def logout(self):
        if self._is_logged_in:
            self._is_logged_in = False
            return "Logout successful"

    @abstractmethod
    def view_all_grades(self):
        pass



