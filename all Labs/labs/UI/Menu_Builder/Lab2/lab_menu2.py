class LabMenu2:
    """
    A class representing the menu for Lab 2.

    Methods:
    - __init__(calculator): Constructor to initialize the class with a calculator object.
    - run(): Run the menu.
    - user_interface(): Display the user interface for Lab 2.
    - get_operator(): Get a valid operator from the user.

    """
    def __init__(self, calculator):
        """
        Constructor to initialize the class with a calculator object.

        :param calculator: An instance of the Calculator class.

        """
        self.calculator = calculator

    def run(self):
        """
        Run the menu.

        """
        self.user_interface()

    def user_interface(self):
        """
        Display the user interface for Lab 2.

        """
        print("Warning: if you want to use the square root function, it will return only the first number you entered")
        while True:
            print("press 1 to calculate")
            print("press q to exit")
            user_choice = input()

            if user_choice == '1':
                first_input = input("Enter the first number: ")
                second_input = input("Enter the second number: ")
                try:
                    if first_input and second_input:
                        self.calculator.first_input = float(first_input)
                        self.calculator.second_input = float(second_input)
                    else:
                        print("Error: Empty input")
                        continue

                    operator = self.get_operator()
                    self.calculator.operator = operator
                    result = self.calculator.perform_calculation()
                    print(f"Result: {result}")

                except ValueError:
                    print("Error: Invalid input. Please enter valid numbers.")

                except ZeroDivisionError as e:
                    print(f"Error: {e}")

                print("Repeat calculation? (y or n): ")
                user_choice = input()
                if user_choice.lower() != 'y':
                    break
            elif user_choice == 'q':
                return 1

    def get_operator(self):
        """
        Get a valid operator from the user.

        :return: The chosen operator.

        """
        valid_operators = ['+', '-', '*', '/', 'sqrt', '^', '%']
        operator = input("Enter operator (+,-,*,/,sqrt,^,%): ")
        while operator not in valid_operators:
            print("Error: Invalid operator")
            operator = input("Enter a valid operator (+,-,*,/,sqrt,^,%): ")
        return operator
