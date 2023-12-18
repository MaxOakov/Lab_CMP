import logging
from math import sqrt
from datetime import datetime

log_file_path = "/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/logger/logger.log"

class CalculatorOperations:
    """
    A class containing basic calculator operations.

    Attributes:
    - logger: Logger object for logging operations.

    Methods:
    - __init__(): Constructor to configure logging.
    - log_operation(operation_name, result): Log the calculator operation with the provided name and result.
    - add(num1, num2): Add two numbers and log the operation.
    - subtract(num1, num2): Subtract num2 from num1 and log the operation.
    - divide(num1, num2): Divide num1 by num2 and log the operation, handling division by zero.
    - multiply(num1, num2): Multiply two numbers and log the operation.
    - square_root(num): Calculate the square root of a number and log the operation.
    - power(num1, num2): Raise num1 to the power of num2 and log the operation.
    - remainder(num1, num2): Calculate the remainder of num1 divided by num2 and log the operation.

    """
    def __init__(self):
        """
        Constructor to configure logging.

        """
        logging.basicConfig(filename=log_file_path, level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def log_operation(self, operation_name, result):
        """
        Log the calculator operation with the provided name and result.

        :param operation_name: The name of the calculator operation.
        :param result: The result of the calculator operation.

        """
        self.logger.info(f"{operation_name} operation. Result: {result}. Date: {datetime.now()}")

    def add(self, num1, num2):
        """
        Add two numbers and log the operation.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the addition.

        """
        result = float(num1 + num2)
        self.log_operation("Adding", result)
        return result

    def subtract(self, num1, num2):
        """
        Subtract num2 from num1 and log the operation.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the subtraction.

        """
        result = float(num1 - num2)
        self.log_operation("Subtracting", result)
        return result

    def divide(self, num1, num2):
        """
        Divide num1 by num2 and log the operation, handling division by zero.

        :param num1: The numerator.
        :param num2: The denominator.
        :return: The result of the division or None if division by zero.

        """
        try:
            result = num1 / num2
            self.log_operation("Dividing", result)
            return result
        except ZeroDivisionError:
            self.logger.error("Division by zero is not allowed.")
            return None

    def multiply(self, num1, num2):
        """
        Multiply two numbers and log the operation.

        :param num1: The first number.
        :param num2: The second number.
        :return: The result of the multiplication.

        """
        result = float(num1 * num2)
        self.log_operation("Multiplying", result)
        return result

    def square_root(self, num):
        """
        Calculate the square root of a number and log the operation.

        :param num: The number to calculate the square root for.
        :return: The result of the square root or None if the number is negative.

        """
        if num < 0:
            self.logger.error("Square root of a negative number is undefined.")
            return None
        result = float(sqrt(num))
        self.log_operation("Calculating square root", result)
        return result

    def power(self, num1, num2):
        """
        Raise num1 to the power of num2 and log the operation.

        :param num1: The base.
        :param num2: The exponent.
        :return: The result of the power operation.

        """
        result = float(pow(num1, num2))
        self.log_operation("Power", result)
        return result

    def remainder(self, num1, num2):
        """
        Calculate the remainder of num1 divided by num2 and log the operation.

        :param num1: The numerator.
        :param num2: The denominator.
        :return: The remainder of the division.

        """
        result = num1 % num2
        self.log_operation("Calculating remainder", result)
        return result
