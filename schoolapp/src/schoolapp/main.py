
prompt = """
    Welcome
    1. login
    2.register
"""
login_prompt= """
    1.login as An instructor
    2. login as A student
"""
registration_prompt ="""
1. register as an instructor
2. register as a Student
"""

def userInput(prompt):
    return input(prompt)


def registration_menu():
    return input(registration_prompt)

def login_menu():
    match input(login_prompt) :
        pass
        # case "1":login_asa_Instructor()


def first_menu():
    match userInput(prompt):
        case '1': login_menu()
        case '2': registration_menu()
        case _ :
            print('invalid input')
            first_menu()

