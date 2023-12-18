from math import sqrt
from labs.Shared.CalcOperations.calc_op import CalculatorOperations

class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        """
        Initialize the calculator.

        Sets up an empty list to archive expressions and defaults the decimalNumber to 2.
        """
        self.archiveExpression = []
        self.decimalNumber = 2
        self.calculator_operations = CalculatorOperations()

    def main_menu(self) -> None:
        """Display the main menu options and handle user input."""
        print("Welcome! If you want to use the calculator, press 1")
        print("If you want to see archived expressions, press 2")
        print("If you want to customize this app, press 3: ")
        userInput = input()
        if userInput == '1':
            self.user_input()
        elif userInput == '2':
            self.show_archived_expressions()
        elif userInput == '3':
            self.show_settings()

    def user_input(self) -> None:
        """Get user input for two numbers and an operator."""
        firstInput = float(input("Enter the first number: "))
        secondInput = float(input("Enter the second number: "))
        operator = input("Enter the operator symbol: ")
        self.error_handler(firstInput, secondInput, operator)
        self.check_correct_operator(operator)
        self.start_calculation(firstInput, secondInput, operator)

    def start_calculation(self, num1: float, num2: float, operator: str) -> None:
        """
        Perform the calculation based on the provided numbers and operator.

        :param num1: The first number in the calculation.
        :param num2: The second number in the calculation.
        :param operator: The operator symbol for the calculation.
        :return: None
        """
        result = 0
        if operator == '+':
            result = self.calculator_operations.add(num1, num2)
        elif operator == '-':
            result = self.calculator_operations.subtract(num1, num2)
        elif operator == '*':
            result = self.calculator_operations.multiply(num1, num2)
        elif operator == '/':
            if num2 == 0:
                print("Error: Can't divide by zero")
                self.recursive_calculation()
                return
            result = self.calculator_operations.divide(num1, num2)
        elif operator == '^':
            result = self.calculator_operations.power(num1, num2)
        elif operator == 'sqrt':
            userChoice = int(input("This operator requires only one number. Press 1 or 2 for the needed number: "))
            if userChoice == 1:
                result = self.calculator_operations.square_root(num1)
            elif userChoice == 2:
                result = self.calculator_operations.square_root(num2)
            else:
                print("Wrong answer. You can only choose number one or two")
                self.recursive_calculation()
                return
        elif operator == '%':
            result = self.calculator_operations.remainder(num1, num2)
        else:
            print("Invalid operator entered, please try again")
            self.recursive_calculation()
            return

        print(f"{num1} {operator} {num2} = {result}")
        self.archive_expression(num1, operator, num2, result)

    def check_correct_operator(self, o: str) -> None:
        """
        Check if the entered operator is valid.

        :param o: The operator to check.
        :return: None
        """
        operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
        if o not in operators:
            print("Invalid operator entered, please try again")
            self.user_input()

    def recursive_calculation(self) -> None:
        """
        Prompt the user if they want to repeat the calculation.

        :return: None
        """
        answer = input("Repeat the calculation? (y or n)")
        if answer == 'y':
            self.user_input()
        elif answer == 'n':
            self.main_menu()
        else:
            print("Error: No such option. Please select y or n")
            self.recursive_calculation()

    def error_handler(self, numOne: float, numTwo: float, op: str) -> None:
        """
        Handle potential errors in user input.

        :param numOne: The first number.
        :param numTwo: The second number.
        :param op: The operator.
        :return: None
        """
        if (numOne == 0 or numTwo == 0) and op == '/':
            print("Error: can't divide by zero")
            self.recursive_calculation()

    def archive_expression(self, firstNumber: float, operator: str, secondNumber: float, result: float) -> None:
        """
        Archive the expression based on user input.

        :param firstNumber: The first number in the expression.
        :param operator: The operator symbol.
        :param secondNumber: The second number in the expression.
        :param result: The result of the expression.
        :return: None
        """
        expressionTemplate = f"{firstNumber} {operator} {secondNumber} = {result}"
        userAnswer = input("Do you want to save expression? (y or n)")
        if userAnswer == 'y':
            self.archiveExpression.append(expressionTemplate)
            self.recursive_calculation()
        if userAnswer == 'n':
            self.recursive_calculation()

    def show_archived_expressions(self) -> None:
        """Display the archived expressions or a message if the archive is empty."""
        if len(self.archiveExpression) == 0:
            print("Archive is empty!")
            self.main_menu()
        for savedExpressions in self.archiveExpression:
            print(savedExpressions)
        self.main_menu()

    def show_settings(self) -> None:
        """Display options for changing settings."""
        print("if you want to delete archive of expressions press 1")
        print("Change rounding by pressing 2: ")
        userInput = input()
        if userInput == '1':
            self.archiveExpression.clear()
            self.main_menu()
        elif userInput == '2':
            self.decimalNumber = int(input("Enter the desired number: "))
            if not 0 <= self.decimalNumber <= 10:
                print("Incorrect number! Enter a valid number between 0 and 10.")
            else:
                print("Rounding successful")
                self.main_menu()
