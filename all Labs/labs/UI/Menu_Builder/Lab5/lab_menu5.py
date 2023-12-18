from labs.classes.Lab5.console_rectangle import ConsoleRectangle

class ConsoleInterface:
    """
    A class representing the console interface for Lab 5.

    Attributes:
    - None

    Methods:
    - __init__(): Constructor for ConsoleInterface class.
    - run(): Run the console interface.
    - print_interface(): Display the interface options.
    - save_object(rectangle): Save the rectangle object to a file.

    """
    def __init__(self):
        """
        Constructor for ConsoleInterface class.

        """
        pass

    def run(self):
        """
        Run the console interface.

        """
        self.print_interface()

    def print_interface(self):
        """
        Display the interface options.

        """
        rectangle = ConsoleRectangle()

        print("if you want to draw a rectangle, press 1: ")
        print("if you want to exit, press f:")
        user_choice = input()

        if user_choice == '1':
            rectangle.run()
            self.save_object(rectangle)
        elif user_choice == 'f':
            return 1

    def save_object(self, rectangle):
        """
        Save the rectangle object to a file.

        :param rectangle: The rectangle object to save.

        """
        filename = input("Enter the filename to save the object: ")
        rectangle.save_object(rectangle, filename)
