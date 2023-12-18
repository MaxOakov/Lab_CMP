from labs.classes.Lab1.task_complition import Calculator

class LabMenu1:
    """
    A class representing the menu for Lab 1.

    Methods:
    - __init__(): Constructor to initialize the class.
    - run(): Run the menu.

    """
    def __init__(self):
        """
        Constructor to initialize the class.

        """
        self.calculator = Calculator()

    def run(self):
        """
        Run the menu.

        """
        print("Welcome to the Calculator App!")
        while True:
            print("Choose an option:")
            print("1. Use Calculator")
            print("2. Exit")
            choice = input()

            if choice == '1':
                self.calculator.main_menu()
            elif choice == '2':
                print("Exiting Calculator App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
