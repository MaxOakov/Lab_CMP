from colorama import Fore, init
from tabulate import tabulate
from labs.classes.Lab7.display_dog_api import DisplayDogApi
from labs.Shared.SaveFormats.save_formats import SaveInFormat
import sys

init(autoreset=True)
DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab7'


class MenuLab7:
    """
    A class representing the menu for Lab 7.

    Attributes:
    - saver (save_in_format): An instance of the save_in_format class.

    Methods:
    - __init__(): Constructor for MenuLab7 class.
    - display_table(data, color): Display the data in table format with the specified color.
    - display_list(data, color): Display the data in list format with the specified color.
    - signal_handler(sig, frame): Handle the Ctrl+C signal.
    - choose_display_format(): Prompt the user to choose a display format.
    - choose_color(): Prompt the user to choose a color.
    - start_menu(): Display the initial menu and prompt the user to choose an option.
    - fetch_dog_breeds(): Fetch dog breeds using DisplayDogApi.
    - display_format_choice(breeds): Prompt the user to choose a display format and display the breeds accordingly.
    - save_data(breeds): Prompt the user to save the data in a specific format.
    - main(): The main function to run the program.

    """
    def __init__(self):
        """
        Constructor for MenuLab7 class.

        """
        self.saver = SaveInFormat()

    @staticmethod
    def display_table(data, color):
        """
        Display the data in table format with the specified color.

        Args:
        - data (list): A list of data to display.
        - color (str): The color for the display.

        """
        headers = [Fore.RESET + color + "Dog Breed", Fore.RESET + color + "PictureUrl"]
        rows = [(color + breed, DisplayDogApi.get_random_image(breed)) for breed in data]
        print(tabulate(rows, headers, tablefmt="grid"))

    @staticmethod
    def display_list(data, color):
        """
        Display the data in list format with the specified color.

        Args:
        - data (list): A list of data to display.
        - color (str): The color for the display.

        """
        for breed in data:
            print(color + f"{breed}: {DisplayDogApi.get_random_image(breed)}")

    @staticmethod
    def signal_handler(sig, frame):
        """
        Handle the Ctrl+C signal.

        Args:
        - sig: The signal number.
        - frame: The current stack frame.

        """
        print("You pressed Ctrl+C!")
        sys.exit(0)

    @staticmethod
    def choose_display_format():
        """
        Prompt the user to choose a display format.

        Returns:
        - str: The user's choice of display format.

        """
        while True:
            print("Choose a display format:")
            print("1. Table")
            print("2. List")
            format_choice = input("Enter the number of the display format: ")

            if format_choice in ("1", "2"):
                return format_choice
            else:
                print("Invalid display format. Please enter 1 or 2.")

    @staticmethod
    def choose_color():
        """
        Prompt the user to choose a color.

        Returns:
        - str: The chosen color.

        """
        while True:
            print("Choose a color:")
            print("1. Red")
            print("2. Green")
            print("3. Yellow")
            color_choice = input("Enter the number of the color: ")

            if color_choice == "1":
                return Fore.RED
            elif color_choice == "2":
                return Fore.GREEN
            elif color_choice == "3":
                return Fore.YELLOW
            else:
                print("Invalid color choice. Please enter 1, 2, or 3.")

    @staticmethod
    def start_menu():
        """
        Display the initial menu and prompt the user to choose an option.

        Returns:
        - str: The user's choice of menu option.

        """
        print("Hello! Choose the option:")
        print("1. Continue")
        print("2. Exit")
        option = input("Enter the number of the option: ")
        return option

    def fetch_dog_breeds(self):
        """
        Fetch dog breeds using DisplayDogApi.

        Returns:
        - list: A list of fetched dog breeds.

        """
        print("Fetching dog breeds...")
        breeds = DisplayDogApi.get_all_breeds()
        print(f"Received {len(breeds)} breeds.")
        return breeds

    def display_format_choice(self, breeds):
        """
        Prompt the user to choose a display format and display the breeds accordingly.

        Args:
        - breeds (list): A list of dog breeds.

        """
        color = self.choose_color()
        format_choice = self.choose_display_format()

        if format_choice == "1":
            print("Displaying table...")
            self.display_table(breeds, color)
        elif format_choice == "2":
            print("Displaying list...")
            self.display_list(breeds, color)

    def save_data(self, breeds):
        """
        Prompt the user to save the data in a specific format.

        Args:
        - breeds (list): A list of dog breeds.

        """
        save_choice = input("Do you want to save the data? (y/n): ")
        if save_choice.lower() == 'y':
            save_format = input("Choose a save format:\n1. JSON\n2. CSV\n3. TXT\nEnter the number of the save format: ")
            save_filename = input("Enter the filename: ")
            if save_format == "1":
                self.saver.save_to_json(breeds, DataPath, save_filename)
            elif save_format == "2":
                self.saver.save_to_csv(breeds, DataPath, save_filename)
            elif save_format == "3":
                self.saver.save_to_txt(breeds, DataPath, save_filename)
            else:
                print("Invalid save format. Please enter 1, 2, or 3.")

    def main(self):
        """
        The main function to run the program.

        """
        while True:
            user_option = self.start_menu()

            if user_option == "1":
                breeds = self.fetch_dog_breeds()
                self.display_format_choice(breeds)
                self.save_data(breeds)

                repeat_choice = input("Do you want to perform another operation? (y/n): ")
                if repeat_choice.lower() != 'y':
                    break
            elif user_option == "2":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please enter 1 or 2.")
