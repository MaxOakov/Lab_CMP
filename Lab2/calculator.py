from decimal import Decimal, InvalidOperation


class Calculator:
    def __init__(self):
        self.operation_history = []

    @staticmethod
    def get_valid_decimal_input(prompt):
        while True:
            user_input = input(prompt).replace(',', '.')
            try:
                return Decimal(user_input)
            except InvalidOperation:
                print(f"Error: Invalid input. Please enter a valid number.")

    def user_input(self):
        num1 = self.get_valid_decimal_input("Enter the first number: ")
        operator = input("Enter the operation (+, -, *, /, ^, √, %): ")
        while operator not in ['+', '-', '*', '/', '^', '√', '%']:
            print("Error: Unknown operation. Please enter a valid operation.")
            operator = input("Enter the operation (+, -, *, /, ^, √, %): ")

        if operator in ['√', '%']:
            num2 = self.get_valid_decimal_input("Enter a number: ")
            self.perform_unary_operation(operator, num1, num2)
        else:
            num2 = self.get_valid_decimal_input("Enter the second number: ")
            self.perform_binary_operation(num1, operator, num2)

    def perform_binary_operation(self, num1, operator, num2):
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2
            elif operator == '^':
                result = num1 ** num2
            else:
                print("Error: Invalid operator.")
                return

            formatted_result = "{:.2f}".format(result)
            print(f'Calculation result: {formatted_result}')
            self.operation_history.append(formatted_result)
        except InvalidOperation:
            print("Error: Invalid input. Please enter valid numbers.")

    def perform_unary_operation(self, operator, num1, num2):
        try:
            if operator == '√':
                if num1 < 0:
                    print("Error: Square root of a negative number is not allowed.")
                    return
                result = num1 ** (1 / num2)
                formatted_result = "{:.2f}".format(result)
                print(f'{operator} of {num1} is: {formatted_result}')
                self.operation_history.append(f'{operator} of {num1} is: {formatted_result}')
            elif operator == '%':
                result = num1 % num2
                formatted_result = "{:.2f}".format(result)
                print(f'Remainder of {num1} is: {formatted_result}')
                self.operation_history.append(f'Remainder of {num1} is: {formatted_result}')
        except InvalidOperation:
            print("Error: Invalid input. Please enter valid numbers.")

    def view_history(self):
        print("\nOperation History:")
        for operation in self.operation_history:
            print(operation)

    def perform_another_calculation(self):
        while True:
            self.user_input()
            another = input("Do you want to perform another calculation? (yes/no): ")
            if another.lower() != "yes":
                break
        self.view_history()
