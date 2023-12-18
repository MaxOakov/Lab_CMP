import pyfiglet

class ASCIIArtGenerator:
    """
    A class for generating ASCII art using pyfiglet.
    """

    def __init__(self):
        """
        Initialize the ASCIIArtGenerator with a list of available fonts.
        """
        self.fonts = ['standard', 'banner', 'slant', 'starwars']

    def generate_ascii_art(self, text: str, selected_font: str, width: int, height: int, char_set: str = None) -> str:
        """
        Generate ASCII art for the given text using the specified parameters.

        :param text: The text to be converted to ASCII art.
        :param selected_font: The selected font for the ASCII art.
        :param width: The desired width of the ASCII art.
        :param height: The desired height of the ASCII art.
        :param char_set: A custom character set to use for rendering. If not provided, the default character set is used.
        :return: The generated ASCII art.
        """
        # Create a pyfiglet Figlet instance with the selected font
        ascii_art = pyfiglet.Figlet(font=selected_font)

        # Render the text using pyfiglet
        ascii_text = ascii_art.renderText(text)

        # Split the rendered text into lines
        ascii_lines = ascii_text.split('\n')

        # Prepare a list to store scaled ASCII lines
        scaled_ascii_lines = []

        # Calculate the length of the custom character set
        char_set_length = len(char_set) if char_set else 0

        # Iterate through each line in the ASCII art
        for line in ascii_lines:
            scaled_line = ""

            # Iterate through each character in the line
            for char in line:
                # If the character is a space, keep it as is
                if char == ' ':
                    scaled_line += ' '
                else:
                    # If a custom character set is provided, use it; otherwise, use the original character
                    if char_set:
                        scaled_line += char_set[hash(char) % char_set_length]
                    else:
                        scaled_line += char

            # Center the line and truncate it to the desired width
            scaled_ascii_lines.append(scaled_line.center(width)[:width])

        # Join the scaled lines and truncate to the desired height
        scaled_ascii_text = '\n'.join(scaled_ascii_lines[:height])

        return scaled_ascii_text
