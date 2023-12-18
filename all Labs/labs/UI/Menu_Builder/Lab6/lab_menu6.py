import unittest
from labs.classes.Lab6.calculator_test import CalculatorArithmeticTester

class LabMenu6:
    """
    A class representing the menu for Lab 6.

    Attributes:
    - None

    Methods:
    - __init__(): Constructor for LabMenu6 class.
    - run_tests(): Run the CalculatorArithmeticTester test suite and save the results to a file.

    """
    def __init__(self):
        """
        Constructor for LabMenu6 class.

        """
        pass

    def run_tests(self):
        """
        Run the CalculatorArithmeticTester test suite and save the results to a file.

        """
        test_suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorArithmeticTester)

        # Specify the full path to save the test results text file
        file_path = "/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab6/test_results.txt"

        # Create a test runner with output to the specified file path
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                runner = unittest.TextTestRunner(stream=f, verbosity=2)
                runner.run(test_suite)
            print(f"Test results successfully saved to {file_path}")
        except Exception as e:
            print(f"Error: {e}")
