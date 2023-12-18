from colorama import Fore, Style
from labs.classes.Lab3.ascii_art_generator import ASCIIArtGenerator
from labs.Shared.saveASCIIArt.save_ascii_name import SaveAscii
import os

class LabMenu3:
    """
    A class representing the menu for Lab 3.

    Attributes:
    - DataPath (str): The path where the data for Lab 3 is stored.

    Methods:
    - __init__(): Constructor to initialize the class with necessary components.
    - get_user_input(): Get user input for ASCII art generation.
    - show_available_fonts(): Display available font styles.
    - get_font_choice(): Get user choice for font style.
    - show_available_colors(): Display available text colors.
    - get_color_choice(): Get user choice for text color.
    - get_positive_number(prompt): Get a positive number from the user.
    - get_custom_characters(): Get custom characters for ASCII art.
    - preview_ascii_art(ascii_text, selected_color): Preview the generated ASCII art.
    - generate_ascii_art(text, selected_font, selected_color, width, height, char_set=None): Generate ASCII art.
    - ask_save_ascii_art(ascii_text): Ask the user if they want to save the ASCII art.

    """
    DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab3/'

    def __init__(self):
        """
        Constructor to initialize the class with necessary components.

        """
        self.colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.BLACK]
        self.generator = ASCIIArtGenerator()
        self.save_ascii_handler = SaveAscii()

    def get_user_input(self):
        """
        Get user input for ASCII art generation.

        :return: Tuple containing user input for ASCII art generation.

        """
        user_input = input("Enter a word or phrase to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_font_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        width = self.get_positive_number("Enter the width of the ASCII art (number of characters in a line): ")
        height = self.get_positive_number("Enter the height of the ASCII art (number of lines): ")

        use_custom_chars = input("Do you want to choose a special character to create ASCII art? (y/n): ").strip().lower()
        char_set = self.get_custom_characters() if use_custom_chars == 'y' else None

        preview_enabled = input("Want to preview your ASCII art before saving? (y/n): ").strip().lower()

        return user_input, self.generator.fonts[font_choice - 1], self.colors[color_choice - 1], width, height, char_set, preview_enabled

    def show_available_fonts(self):
        """
        Display available font styles.

        """
        print("Available font styles:")
        for i, font in enumerate(self.generator.fonts, start=1):
            print(f"{i}. {font}")

    def get_font_choice(self):
        """
        Get user choice for font style.

        :return: The chosen font style.

        """
        while True:
            try:
                font_choice = int(input("Choose a font style number (1-4): "))
                if 1 <= font_choice <= 4:
                    return font_choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter the correct font style number.")

    def show_available_colors(self):
        """
        Display available text colors.

        """
        print("Available text colors:")
        for i, color in enumerate(self.colors, start=1):
            print(f"{i}. Color {color}")

    def get_color_choice(self):
        """
        Get user choice for text color.

        :return: The chosen text color.

        """
        while True:
            try:
                color_choice = int(input(Fore.RESET + "Choose a text color number (1-4): "))
                if 1 <= color_choice <= 4:
                    return color_choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter the correct text color number.")

    def get_positive_number(self, prompt):
        """
        Get a positive number from the user.

        :param prompt: The prompt to display.

        :return: The positive number entered by the user.

        """
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                else:
                    print("Please enter a number greater than zero.")
            except ValueError:
                print("Please enter the correct number.")

    def get_custom_characters(self):
        """
        Get custom characters for ASCII art.

        :return: The custom characters entered by the user.

        """
        return input("Enter the characters you want to use for ASCII art (e.g., '@#*'): ")

    def preview_ascii_art(self, ascii_text, selected_color):
        """
        Preview the generated ASCII art.

        :param ascii_text: The generated ASCII art.
        :param selected_color: The chosen text color.

        """
        print(selected_color + ascii_text + Style.RESET_ALL)

    def generate_ascii_art(self, text, selected_font, selected_color, width, height, char_set=None):
        """
        Generate ASCII art.

        :param text: The text to convert to ASCII art.
        :param selected_font: The chosen font style.
        :param selected_color: The chosen text color.
        :param width: The width of the ASCII art.
        :param height: The height of the ASCII art.
        :param char_set: Custom characters for ASCII art.

        :return: The generated and colored ASCII art.

        """
        ascii_text = self.generator.generate_ascii_art(text, selected_font, width, height, char_set)
        colored_text = selected_color + ascii_text + Style.RESET_ALL
        return colored_text

    def ask_save_ascii_art(self, ascii_text):
        """
        Ask the user if they want to save the ASCII art.

        :param ascii_text: The ASCII art to save.

        """
        self.save_ascii_handler.ask_save_ascii_art(ascii_text, self.DataPath)
