
class MainMenu:
    def __init__(self):
        self.courses = []
        self.choice =""


    def display_menu(self):
        while self.choice != "6":
            print("\nWelcome to the User Management System")
            print("1. Register as Student")
            print("2. Register as Instructor")
            print("3. Create Course (Instructor)")
            print("4. View Courses (Student)")
            print("5. View Students and Assign Grades (Instructor)")
            print("6. Exit")

            self.choice = input("Enter your choice: ")

            if self.choice == "1":
                print("Student registration page")

