import unittest
from unittest.mock import patch
from labs.classes.Lab2.solutions import Calculator

class CalculatorArithmeticTester(unittest.TestCase):
    """
    Unit tests for arithmetic operations of the Calculator class.
    """

    def setUp(self):
        """
        Set up a Calculator instance for each test case.
        """
        self.calculator = Calculator.Calculator()

    def test_addition(self):
        """
        Test the addition functionality of the Calculator class.
        """
        self.assertEqual(self.calculator.add(5, 5), 10)

    def test_subtraction(self):
        """
        Test the subtraction functionality of the Calculator class.
        """
        self.assertEqual(self.calculator.subtract(10, 3), 7)

    def test_multiplication(self):
        """
        Test the multiplication functionality of the Calculator class.
        """
        self.assertEqual(self.calculator.multiply(12.5, 3.7), 46.25)

    def test_division(self):
        """
        Test the division functionality of the Calculator class.
        """
        self.assertEqual(self.calculator.divide(10, 5), 2)

class CalculatorErrorHandlingTester(unittest.TestCase):
    """
    Unit tests for error handling of the Calculator class.
    """

    def setUp(self):
        """
        Set up a Calculator instance for each test case.
        """
        self.calculator = Calculator.Calculator()

    def test_square_root_negative(self):
        """
        Test handling square root of a negative number.
        """
        self.assertEqual(self.calculator.square_root(-25), "Cannot take the square root of a negative number")

    def test_remainder_divide_by_zero(self):
        """
        Test handling remainder when dividing by zero.
        """
        result = self.calculator.remainder(10, 0)
        self.assertEqual(result, "Can't find the remainder when dividing by zero")

    def test_invalid_operator(self):
        """
        Test handling an invalid operator.
        """
        result = self.calculator.start_calculation()
        self.assertEqual(result, "Invalid operator")

    @patch("builtins.input", side_effect=['', '5'])
    def test_mock_empty_input(self):
        """
        Test handling empty input using mock input.
        """
        result = self.calculator.set_user_input(None, None)
        self.assertEqual(result, "Error: Empty input")

    def test_exception_by_division_by_zero(self):
        """
        Test raising an exception when dividing by zero.
        """
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10,0)
