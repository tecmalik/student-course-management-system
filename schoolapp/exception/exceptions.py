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


class InvalidLoginException:
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PasswordTooShort:
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PasswordNotAccepted:
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidArgumentException:
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class NoCourseAvailableException:
    pass