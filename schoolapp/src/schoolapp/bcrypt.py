import bcrypt

class Bcrypt:
    def encrypt_password(self, password:str) -> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password: str, hashed_password:bytes) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password )


