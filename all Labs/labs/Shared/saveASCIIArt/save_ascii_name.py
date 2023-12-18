import os
from datetime import datetime

class SaveAscii:
    """
    A class for saving ASCII art to a file.

    Methods:
    - __init__(): Constructor to initialize the class.
    - log_save_ascii_art(file_path): Log the information about saving ASCII art to a file.
    - ask_save_ascii_art(ascii_text, data_path): Ask the user if they want to save the ASCII art to a file
      and save it if the user chooses to do so.

    """
    def __init__(self):
        """
        Constructor to initialize the class.

        """
        pass

    def log_save_ascii_art(self, file_path):
        """
        Log the information about saving ASCII art to a file.

        :param file_path: The path where the ASCII art is saved.

        """
        print(f"ASCII art saved to {file_path}. Date: {datetime.now()}")

    def ask_save_ascii_art(self, ascii_text, data_path):
        """
        Ask the user if they want to save the ASCII art to a file and save it if the user chooses to do so.

        :param ascii_text: The ASCII art to be saved.
        :param data_path: The path where the file will be saved.

        """
        try:
            save_option = input("Do you want to save the ASCII art to a file? (y/n): ").strip().lower()
            if save_option != 'y':
                print("ASCII art not saved.")
                return

            file_name = input("Enter the desired file name (e.g., art.txt): ").strip()

            # Construct the file path using data_path
            file_path = os.path.join(data_path, f"{file_name}.txt")

            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists

            with open(file_path, 'w') as file:
                file.write(ascii_text)

            self.log_save_ascii_art(file_path)

        except Exception as e:
            print(f"Error saving ASCII art: {e}")
