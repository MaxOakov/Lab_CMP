import logging
from datetime import datetime


class Main:
    """
        A class representing the main menu for all labs.

        Methods:
        - __init__(): Constructor for Main class.
        - log_user_choice(user_choice): Log the user's choice.
        - display_menu(): Display the main menu.
        - run(): Run the main menu loop and execute corresponding lab menus based on user input.

        """
    def __init__(self):
        """
         Constructor for Main class. Configures logging.

         """
        # Configure logging
        log_file_path = "/Users/olegkuzo/Desktop/політех/2Курс/СМП/SPLLabs/Labs/labs/Data/logger/logger.log"
        logging.basicConfig(filename=log_file_path, level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def log_user_choice(self, user_choice):
        """
        Log the user's choice.

        Args:
        - user_choice (str): The user's menu choice.

        """
        self.logger.info(f"User choice: {user_choice}. Date: {datetime.now()}")

    def display_menu(self):
        """
        Display the main menu.

        """
        for i in range(1, 9):
            print(f"if you want to open lab{i}, press {i}:")
    print("if you want to exit, press q:")

    def run(self):
        """
        Run the main menu loop and execute corresponding lab menus based on user input.

        """
        while True:
            self.display_menu()
            user_choice = input()
            self.log_user_choice(user_choice)

            if user_choice == '1':
                import labs.UI.Menu_Builder.Lab1.lab_menu1 as menu1
                calculator_lab1 = menu1.LabMenu1()
                calculator_lab1.run()

            elif user_choice == '2':
                import labs.UI.Menu_Builder.Lab2.lab_menu2 as menu2
                import labs.classes.Lab2.solutions
                calculator_lab2_instance = labs.classes.Lab2.Calculator()
                calculator = menu2.LabMenu2(calculator_lab2_instance)
                calculator.run()

            elif user_choice == '3':
                import labs.UI.Menu_Builder.Lab3.lab_menu3 as menu3
                ascii_art_generator = menu3.LabMenu3()
                user_input, selected_font, selected_color, width, height, char_set, preview_enabled = ascii_art_generator.get_user_input()
                if preview_enabled == 'y':
                    ascii_text = ascii_art_generator.generate_ascii_art(user_input, selected_font, selected_color,
                                                                        width, height,
                                                                        char_set)
                    ascii_art_generator.preview_ascii_art(ascii_text, selected_color)
                    ascii_art_generator.ask_save_ascii_art(ascii_text)

            elif user_choice == '4':
                import labs.UI.Menu_Builder.Lab4.lab_menu4 as menu4
                import labs.classes.Lab4.ascii_art_generator
                ascii_generator = labs.classes.Lab4.ASCIIArtGenerator.AsciiArtGenerator()
                ascii = menu4.LabMenu4(ascii_generator)
                ascii.run()

            elif user_choice == '5':
                import labs.UI.Menu_Builder.Lab5.lab_menu5 as menu5
                rectangle = menu5.ConsoleInterface()
                rectangle.run()

            elif user_choice == '6':
                import labs.UI.Menu_Builder.Lab6.lab_menu6 as menu6
                tests = menu6.LabMenu6()
                tests.run_tests()

            elif user_choice == '7':
                import labs.UI.Menu_Builder.Lab7.lab_menu7 as menu7
                api_caller = menu7.MenuLab7()
                api_caller.main()

            elif user_choice == '8':
                import labs.UI.Menu_Builder.Lab8.lab_menu8 as menu8
                lab8 = menu8.LabMenu8()
                lab8.run()

            elif user_choice.lower() == 'q':
                break  # Exit the loop if the user enters 'exit' (case-insensitive)

            else:
                print("Invalid choice. Please enter a valid option or 'q' to quit.")


if __name__ == '__main__':
    main_instance = Main()
    main_instance.run()
