import json
import csv
import os
import logging
from colorama import Fore
from labs.classes.Lab7.display_dog_api import DisplayDogApi
from datetime import datetime

log_file_path = "/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/logger/logger.log"

class SaveInFormat:
    """
    A class for saving data in different formats (JSON, CSV, TXT).

    Methods:
    - __init__(): Constructor to initialize the class.
    - remove_color_codes(text): Remove ANSI color codes from the given text.
    - save_to_json(data, directory, filename): Save data in JSON format.
    - save_to_csv(data, directory, filename): Save data in CSV format.
    - save_to_txt(data, directory, filename): Save data in TXT format.

    """
    def __init__(self):
        """
        Constructor to initialize the class.

        """
        # Configure logging
        logging.basicConfig(filename=log_file_path, level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def remove_color_codes(self, text):
        """
        Remove ANSI color codes from the given text.

        :param text: The text from which to remove color codes.
        :return: The text without color codes.

        """
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end + 1:]
            else:
                break
        return text

    def save_to_json(self, data, directory, filename):
        """
        Save data in JSON format.

        :param data: The data to be saved.
        :param directory: The directory where the file will be saved.
        :param filename: The desired filename.

        """
        filepath = os.path.join(directory, filename)

        data_to_save = [{"DogBreed": breed, "PictureUrl": DisplayDogApi.get_random_image(breed)} for breed in data]
        with open(filepath, 'w') as file:
            json.dump(data_to_save, file, indent=2)
        self.logger.info(f"Data saved to {filepath} in JSON format. Date: {datetime.now()}")

    def save_to_csv(self, data, directory, filename):
        """
        Save data in CSV format.

        :param data: The data to be saved.
        :param directory: The directory where the file will be saved.
        :param filename: The desired filename.

        """
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Fore.RESET + "DogBreed", Fore.RESET + "PictureUrl"])
            for breed in data:
                writer.writerow(
                    [self.remove_color_codes(breed), self.remove_color_codes(DisplayDogApi.get_random_image(breed))])
        self.logger.info(f"Data saved to {filepath} in CSV format. Date: {datetime.now()}")

    def save_to_txt(self, data, directory, filename):
        """
        Save data in TXT format.

        :param data: The data to be saved.
        :param directory: The directory where the file will be saved.
        :param filename: The desired filename.

        """
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as file:
            for breed in data:
                file.write(
                    f"{self.remove_color_codes(breed)}: {self.remove_color_codes(DisplayDogApi.get_random_image(breed))}\n")
        self.logger.info(f"Data saved to {filepath} in TXT format. Date: {datetime.now()}")
