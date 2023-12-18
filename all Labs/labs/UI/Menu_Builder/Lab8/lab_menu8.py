from labs.classes.Lab8.csv_visualizer import MockDataVisualizer

class LabMenu8:
    """
    A class representing the menu for Lab 8.

    Methods:
    - __init__(): Constructor for LabMenu8 class.
    - run(): Run the menu and perform operations based on user input.

    """
    def __init__(self):
        """
        Constructor for LabMenu8 class.

        """
        pass

    def run(self):
        """
        Run the menu and perform operations based on user input.

        """
        csv_filepath = '/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/classes/Lab8/mockdata/MOCK_DATA.csv'

        while True:
            data_visualizer = MockDataVisualizer(csv_filepath)

            data_visualizer.explore_data()

            user_choice = input("1. Pie chart\n2. Scatter diagram\n3. Bar chart\n4. Output all charts\nEnter chart number (1-4) or 'x' to exit: ")

            if user_choice.lower() == 'x':
                break

            data_visualizer.visualize_data(user_choice)
