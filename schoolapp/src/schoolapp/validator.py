import re
from email_validator import validate_email
from schoolapp.exception import exceptions
from schoolapp.src.schoolapp.bcrypt import Bcrypt


class Validator:

    def validate_password(self,password: str) -> str:
        if len(password) < 8:
            raise exceptions.PasswordTooShort(Exception)
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&])[A-Za-z\d!@#$%^&]{8,}$"
        if re.match(pattern, password):
            print('password Accepted')
            return password
        else:
            raise exceptions.PasswordNotAccepted("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")


    def validate_email(self, email: str) -> str:
        validate_email(email)
        return email

    # def validate_name(self, first_name:str, last_name:str ):
    #     with open(file, 'r'):
    #         pass


    def validate_duplicate_user(self, users_list, email: str) -> bool:
        return email not in [user.email for user in users_list]
