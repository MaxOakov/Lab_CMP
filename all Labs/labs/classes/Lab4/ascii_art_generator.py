from colorama import Fore, Style
from labs.classes.Lab4.fonts import *  # Assuming the necessary fonts are defined in the 'fonts' module
from labs.Shared.saveASCIIArt.save_ascii_name import save_ascii

class AsciiArtGenerator:
    """
    A class for generating and saving ASCII art with color options.
    """

    DataPath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/Lab4/'

    def __init__(self):
        """
        Initialize the AsciiArtGenerator with fonts, colors, and a save_ascii handler.
        """
        # Dictionary of available fonts
        self.fonts = {
            "standard": standard_dic,
            "starwars": starwars_dic,
            "avatar": avatar_dic,
            "binary": standard_bin_dic
        }

        # List of available colors
        self.colors = [Fore.BLACK, Fore.RED, Fore.BLUE, Fore.YELLOW]

        # Instance of the save_ascii class for handling ASCII art saving
        self.save_ascii_handler = save_ascii()

    def generate_ascii_art(self, text: str, font_choice: int, color_choice: int) -> str:
        """
        Generate ASCII art with the specified text, font, and color.

        :param text: The text to be converted to ASCII art.
        :param font_choice: The index of the selected font.
        :param color_choice: The index of the selected color.
        :return: The generated ASCII art with color.
        """
        # Select the chosen font
        selected_font = list(self.fonts.values())[font_choice]

        # Initialize an empty string to store the ASCII art
        ascii_art = ""

        # Iterate through each line of the selected font
        for line in range(len(selected_font['a'].split('\n'))):
            # Iterate through each character in the input text
            for char in text:
                # Check if the character is a letter
                if char.isalpha():
                    # Check if the character is available in the selected font
                    if char in selected_font:
                        # Append the corresponding line of the character from the font to the ASCII art
                        ascii_art += selected_font[char].split('\n')[line]
                    else:
                        # Default space if character is not available
                        ascii_art += " " * 5
                else:
                    # Move to the next line for non-letter characters
                    ascii_art += "\n"

            # Move to the next line after completing a line of characters
            ascii_art += "\n"

        # Apply the selected color to the ASCII art
        return self.colors[color_choice] + ascii_art + Style.RESET_ALL

    def ask_save_ascii_art(self, ascii_text: str):
        """
        Ask the user if they want to save the generated ASCII art.

        :param ascii_text: The generated ASCII art to be saved.
        :return: None
        """
        self.save_ascii_handler.ask_save_ascii_art(ascii_text, self.DataPath)
