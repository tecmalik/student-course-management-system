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



class User(ABC):
    def __init__(self, name: str ,email: str, password: str ):
        self._name = name
        self._email = validate_email(email)
        self.__password = password

    @property
    def name(self):
        return self._name


    @abstractmethod
    def generate_id(self):
        pass

    @abstractmethod
    def login(self, email, password):
        pass

    @name.setter
    def name(self, value):
        self._name = value
