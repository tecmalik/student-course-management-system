import re


class Validator:
    def validate_password(self,password: str) -> bool:
        return len(password) >= 8 and any(paswd.isdigit() for paswd in password)

    def validate_username(self, username: str) -> bool:
        return bool(re.match(r"^[a-zA-Z0-9_.-]{3,20}$", username))

    def validate_email(self, email: str) -> bool:
        return bool(re.match(r"^[a-zA-Z0-9_.+-]+@gmail\.com$", email))

    def validate_duplicate_user(self, users_list, email: str) -> bool:
        return email not in [user.email for user in users_list]
