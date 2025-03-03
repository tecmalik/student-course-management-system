import re
from abc import abstractmethod, ABC
from logging import raiseExceptions


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



