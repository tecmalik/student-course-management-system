
class MainMenu:
    prompt = """
        Welcome
        1. login
        2.register
    """
    registration_prompt = """
        1. register as An instructor
        2. register as A student
    """
    instructor_prompt = """
        1. create courses
        2. view created courses instructor
        3. assign grades to Student
        4. view registered students
    """

    def userInput(prompt):
        return input(prompt)

    student_prompt = """
        1. enroll for a course
        2. view available courses
        3. view grades  
        """

    def instructor_login():
        try:
            userInput("Enter username to login: ")
            userInput("Enter password to login: ")

        except Exception as err:
            print(err)
        finally:
            instructors_menu()