class InvalidLoginDetails(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCourseDetails(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ExistingLogInDetails(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PasswordTooShort(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PasswordNotAccepted(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidEmail(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseAlreadyExist(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseDoesNotExist(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class UserAlreadyExist(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidLoginException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidArgumentException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NoCourseAvailableException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



