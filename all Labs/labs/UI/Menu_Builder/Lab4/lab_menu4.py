from colorama import Fore, Style
from labs.Shared.saveASCIIArt.save_ascii_name import SaveAscii

class LabMenu4:
    """
    A class representing the menu for Lab 4.

    Attributes:
    - DataPath (str): The path where the data for Lab 4 is stored.

    Methods:
    - __init__(ascii_art_generator): Constructor to initialize the class with the ASCII art generator.
    - run(): Run the menu for Lab 4.
    - get_user_input(): Get user input for ASCII art generation.
    - show_available_fonts(): Display available font styles.
    - get_font_choice(): Get user choice for font style.
    - show_available_colors(): Display available text colors.
    - get_color_choice(): Get user choice for text color.
    - preview_ascii_art(ascii_text, selected_color): Preview the generated ASCII art.
    - ask_save_ascii_art(ascii_text, DataPath): Ask the user if they want to save the ASCII art.

    """
    DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab4/'

    def __init__(self, ascii_art_generator):
        """
        Constructor to initialize the class with the ASCII art generator.

        :param ascii_art_generator: The ASCII art generator.

        """
        self.ascii_art_generator = ascii_art_generator
        self.save_ascii_handler = SaveAscii()

    def run(self):
        """
        Run the menu for Lab 4.

        """
        user_input, font_choice, color_choice = self.get_user_input()
        ascii_text = self.ascii_art_generator.generate_ascii_art(user_input, font_choice, color_choice)
        self.preview_ascii_art(ascii_text, self.ascii_art_generator.colors[color_choice])

        self.ask_save_ascii_art(ascii_text, self.DataPath)

    def get_user_input(self):
        """
        Get user input for ASCII art generation.

        :return: Tuple containing user input for ASCII art generation.

        """
        user_input = input("Enter a word to convert to ASCII art: ")

        self.show_available_fonts()
        font_choice = self.get_font_choice()

        self.show_available_colors()
        color_choice = self.get_color_choice()

        return user_input, font_choice, color_choice

    def show_available_fonts(self):
        """
        Display available font styles.

        """
        print("Available Fonts:")
        for font_name in self.ascii_art_generator.fonts.keys():
            print(f" - {font_name}")

    def get_font_choice(self):
        """
        Get user choice for font style.

        :return: The chosen font style.

        """
        while True:
            try:
                font_choice = int(input("Choose a font style number (0-3): "))
                if 0 <= font_choice <= 3:
                    return font_choice
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Please enter the correct font style number.")

    def show_available_colors(self):
        """
        Display available text colors.

        """
        print("Available Colors:")
        for i, color in enumerate(self.ascii_art_generator.colors):
            print(f"{i} - {color}")

    def get_color_choice(self):
        """
        Get user choice for text color.

        :return: The chosen text color.

        """
        while True:
            try:
                color_choice = int(input(Fore.RESET + "Choose a text color number (0-3): "))
                if 0 <= color_choice <= 3:
                    return color_choice
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Please enter the correct text color number.")

    def preview_ascii_art(self, ascii_text, selected_color):
        """
        Preview the generated ASCII art.

        :param ascii_text: The generated ASCII art.
        :param selected_color: The chosen text color.

        """
        print(selected_color + ascii_text + Style.RESET_ALL)

    def ask_save_ascii_art(self, ascii_text, DataPath):
        """
        Ask the user if they want to save the ASCII art.

        :param ascii_text: The ASCII art to save.
        :param DataPath: The path to save the ASCII art.

        """
        self.save_ascii_handler.ask_save_ascii_art(ascii_text, DataPath)
