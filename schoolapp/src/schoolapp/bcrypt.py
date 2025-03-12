
import bcrypt


class Bcrypt:
    def encrypt_password(self, password: str) -> bytes:
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password: str, hashed_password: str) -> bool:
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    def validate_username(username, password):
        with open(file, 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(':')
                if username == stored_username:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

import bcrypt

