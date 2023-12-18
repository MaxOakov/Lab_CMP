from labs.classes.Lab5.rectangle import Rectangle

class ConsoleRectangle(Rectangle):
    """
    A class for interacting with the user to configure and display a Rectangle object.
    """

    figure = Rectangle

    @classmethod
    def set_parameters(cls, dct, input_message):
        """
        Helper method to display available parameters and let the user select one.

        :param dct: A dictionary of available parameters.
        :param input_message: A message to prompt the user.
        :return: The selected parameter value or None if not found.
        """
        for key, value in dct.items():
            print(f"{key}: {value}")
        selected_value = input(f"Select {input_message}: ")
        current_value = dct.get(selected_value, None)
        if current_value:
            return current_value
        else:
            return None

    def input_function(self, dct, input_message, default):
        """
        Prompt the user if they want to set a parameter and call set_parameters if desired.

        :param dct: A dictionary of available parameters.
        :param input_message: A message to prompt the user.
        :param default: The default value if the user chooses not to set the parameter.
        :return: The selected parameter value or the default if not set.
        """
        check = input(f"Do you want to set {input_message}? (y/n): ")
        parameter_value = None
        if check == 'y':
            parameter_value = self.set_parameters(dct, input_message)
        if parameter_value:
            return parameter_value
        else:
            return default

    def configuration(self):
        """
        Configure the Rectangle object based on user input.
        """
        rect_to_draw = Rectangle()
        self.size_x = int(input("Input size_x: "))
        self.size_y = int(input("Input size_y: "))
        self.size_z = int(input("Input size_z: "))

        self._color_1 = self.input_function(self._COLORS, 'color_1', self._color_1)
        self._color_2 = self.input_function(self._COLORS, 'color_2', self._color_2)
        self._color_3 = self.input_function(self._COLORS, 'color_3', self._color_3)

        change_space = input('Do you want to create space? (y/n): ')
        if change_space == 'y':
            space = int(input("Input space: "))
            self._space(space)

        change_zoom = input('Do you want to create zoom? (y/n): ')
        if change_zoom == 'y':
            self._zoom = int(input("Input zoom: "))
            self.set_zoom()

    def save_object(self, obj, filename):
        """
        Save the object to a text file.

        :param obj: The object to save.
        :param filename: The filename for the saved object.
        """
        try:
            with open(f"{filename}.txt", 'w') as file:
                for line in obj:
                    file.write(str(line) + "\n")
            print(f"Object saved successfully to {filename}.txt")
        except Exception as e:
            print(f"Error occurred while saving: {e}")

    def run(self):
        """
        Run the configuration and display loop until the user decides to exit.
        """
        stop = ''
        while stop.lower() != 'f':
            try:
                self.configuration()
                self.create()
                print(self)
            except Exception as e:
                print(e)
            finally:
                stop = input("Press 'f' if you want to exit: ")
