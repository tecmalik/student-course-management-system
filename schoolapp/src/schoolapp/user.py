class User:
    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_logged_in = False

    def register(self, first_name: str, last_name: str, email: str, password: str):
        return User(first_name, last_name, email, password)

    def login(self, email: str, password: str):
        if self.email == email and self.password == password:
            self.is_logged_in = True
            return "Login successful"
        else:
            return "Invalid email or password"

    def logout(self):
        if self.is_logged_in:
            self.is_logged_in = False
            return "Logout successful"
        else:
            return "User is already logged out"

