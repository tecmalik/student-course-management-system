import re
from email_validator import validate_email
from schoolapp.exception import exceptions
from schoolapp.exception.exceptions import InvalidArgumentException, PasswordTooShort, PasswordNotAccepted
from schoolapp.src.schoolapp.bcrypt import Bcrypt


class Validator:

    def validate_password(self,password: str) -> str:
        if " " in password :
            raise InvalidArgumentException("email cannot contain space")
        if password.isspace():
            raise InvalidArgumentException("password can not be empty.")
        if len(password) < 8:
            raise PasswordTooShort("password must be at least 8 characters long")
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
        if re.match(pattern, password):
            print('password Accepted')
            return password
        else:
            raise PasswordNotAccepted("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")


    def validate_email(self, email: str) -> str:
        forbidden_chars = "!#$%^*()+,: ;<>?[]\\{}|~&=_'"
        count = 0
        for char in email:
            if char == '@':
                count += 1
        if count > 1 :
            raise ValueError("invalid character(s) in email")
        if any(char in forbidden_chars for char in email):
            raise ValueError("invalid character(s) in email")
        if " " in email:
            raise InvalidArgumentException("email cannot contain space")

        validate_email(email)
        return email

    def validate_name(self, first_name:str, last_name:str ):
        if first_name.isspace():
            raise InvalidArgumentException("First name cannot be empty")
        if last_name.isspace():
            raise InvalidArgumentException("Last name name cannot be empty")

