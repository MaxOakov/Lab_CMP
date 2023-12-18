import requests

class DisplayDogApi:
    """
    A class to interact with the Dog API and display information about dog breeds and random dog images.
    """

    BASE_URL = "https://dog.ceo/api"

    @classmethod
    def get_all_breeds(cls):
        """
        Get a list of all dog breeds available in the Dog API.

        :return: A list of dog breeds.
        """
        response = requests.get(f"{cls.BASE_URL}/breeds/list/all")
        data = response.json()
        breeds = data.get("message", {})
        return breeds.keys()

    @classmethod
    def get_random_image(cls, breed):
        """
        Get a random image URL for a specific dog breed.

        :param breed: The dog breed for which to get a random image.
        :return: The URL of a random dog image.
        """
        response = requests.get(f"{cls.BASE_URL}/breed/{breed}/images/random")
        data = response.json()
        image_url = data.get("message", "")
        return image_url
