import unittest
from unittest.mock import patch, MagicMock
from display_dog_api import DisplayDogApi
from labs.UI.Menu_Builder.Lab7.lab_menu7 import MenuLab7

class TestDisplayDogApi(unittest.TestCase):
    """
    A test class for testing the DisplayDogApi and MenuLab7 classes.

    Methods:
    - test_get_all_breeds: Test the get_all_breeds method of DisplayDogApi class.
    - test_invalid_display_format: Test the choose_display_format method of MenuLab7 class.

    """
    @patch('requests.get')
    def test_get_all_breeds(self, mock_requests_get):
        """
        Test the get_all_breeds method of DisplayDogApi class.

        This method uses the @patch decorator to mock the requests.get method
        and simulate the API response.

        The mock_response is configured to return a dictionary simulating the API response.
        The test then calls DisplayDogApi.get_all_breeds() and checks if the returned breeds
        match the expected list.

        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": {"breed1": {}, "breed2": {}}}
        mock_requests_get.return_value = mock_response

        breeds = DisplayDogApi.get_all_breeds()

        self.assertEqual(list(breeds), ["breed1", "breed2"])

    @patch('builtins.input', side_effect=['3'])
    def test_invalid_display_format(self):
        """
        Test the choose_display_format method of MenuLab7 class.

        This method uses the @patch decorator to mock the builtins.input method
        and simulate user input ('3').

        The test then calls MenuLab7.choose_display_format() and checks if the expected
        exception (ValueError or StopIteration) is raised.

        """
        with self.assertRaises((ValueError, StopIteration)):
            MenuLab7.choose_display_format()
