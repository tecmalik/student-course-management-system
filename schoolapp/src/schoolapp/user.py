import re
from abc import abstractmethod, ABC


def validate_password(password):
    pattern = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
    if re.match(pattern, password):
        return password
    else:
        raise Exception("Invalid password")

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return email
    else:
        raise Exception("Invalid email")



class User (ABC):
    def _init_(self, name ,email, password ):
        self._name = name
        self._email = validate_email(email)
        self.__password = validate_password(password)


    @abstractmethod
    @property
    def name(self):
        return self._name

    def generate_id(self):
        pass