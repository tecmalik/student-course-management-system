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
pattern_password = r"^(?=.[A-Z])(?=.[a-z])(?=.\d)(?=.[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
class User(ABC):
    def __init__(self, name: str ,email: str, password: str ):
        self._name = name
        self._email = validate_email(email)
        self.__password = password

    @property
    def name(self):
        return self._name

    @abstractmethod
    def login(self, email, password):
        return self.email == email and self.password == password

    @name.setter
    def name(self, value):
        self._name = value

    def register(self, email, password, name):
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format.")
        if not re.match(pattern_password, password):
            raise ValueError("Password must be at least 8 characters with one letter and one number.")
        self.email = email
        self.password = password
        self.name = name
        return True