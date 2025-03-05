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


