from labs.Shared.CalcOperations.calc_op import CalculatorOperations

class Calculator:
    """
    A simple calculator class that uses CalculatorOperations for basic arithmetic operations.
    """

    def __init__(self):
        """
        Initialize the calculator.

        Sets up input values and an instance of CalculatorOperations for performing calculations.
        """
        self.first_input = None
        self.second_input = None
        self.operator = None
        self.calc_operations = CalculatorOperations()

    def perform_calculation(self):
        """
        Perform the calculation based on the stored inputs and operator.

        :return: The result of the calculation.
        """
        return self.start_calculation()

    def check_input(self):
        """
        Check for valid input conditions.

        :return: A string indicating the validation result.
        """
        if self.first_input == '' or self.second_input == '':
            return "Empty input"
        if (self.first_input == 0 or self.second_input == 0) and self.operator == '/':
            return "Can't divide by zero"

    def start_calculation(self):
        """
        Start the calculation based on the stored inputs and operator.

        :return: The result of the calculation.
        """
        if self.operator == '+':
            return self.calc_operations.add(self.first_input, self.second_input)
        elif self.operator == '-':
            return self.calc_operations.subtract(self.first_input, self.second_input)
        elif self.operator == '*':
            return self.calc_operations.multiply(self.first_input, self.second_input)
        elif self.operator == '/':
            return self.calc_operations.divide(self.first_input, self.second_input)
        elif self.operator == 'sqrt':
            return self.calc_operations.square_root(self.first_input)
        elif self.operator == '^':
            return self.calc_operations.power(self.first_input, self.second_input)
        elif self.operator == '%':
            return self.calc_operations.remainder(self.first_input, self.second_input)
        else:
            return "Invalid operator"
from labs.Shared.CalcOperations.calc_op import CalculatorOperations

class Calculator:
    """
    A simple calculator class that uses CalculatorOperations for basic arithmetic operations.
    """

    def __init__(self):
        """
        Initialize the calculator.

        Sets up input values and an instance of CalculatorOperations for performing calculations.
        """
        self.first_input = None
        self.second_input = None
        self.operator = None
        self.calc_operations = CalculatorOperations()

    def perform_calculation(self):
        """
        Perform the calculation based on the stored inputs and operator.

        :return: The result of the calculation.
        """
        return self.start_calculation()

    def check_input(self):
        """
        Check for valid input conditions.

        :return: A string indicating the validation result.
        """
        if self.first_input == '' or self.second_input == '':
            return "Empty input"
        if (self.first_input == 0 or self.second_input == 0) and self.operator == '/':
            return "Can't divide by zero"

    def start_calculation(self):
        """
        Start the calculation based on the stored inputs and operator.

        :return: The result of the calculation.
        """
        if self.operator == '+':
            return self.calc_operations.add(self.first_input, self.second_input)
        elif self.operator == '-':
            return self.calc_operations.subtract(self.first_input, self.second_input)
        elif self.operator == '*':
            return self.calc_operations.multiply(self.first_input, self.second_input)
        elif self.operator == '/':
            return self.calc_operations.divide(self.first_input, self.second_input)
        elif self.operator == 'sqrt':
            return self.calc_operations.square_root(self.first_input)
        elif self.operator == '^':
            return self.calc_operations.power(self.first_input, self.second_input)
        elif self.operator == '%':
            return self.calc_operations.remainder(self.first_input, self.second_input)
        else:
            return "Invalid operator"
