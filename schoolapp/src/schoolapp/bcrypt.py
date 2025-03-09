import hashlib


class Bcrypt:
    def encrypt_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def decrypt_password(self, password: str) -> str:
        raise NotImplementedError("Password decryption is not supported for hashed passwords")