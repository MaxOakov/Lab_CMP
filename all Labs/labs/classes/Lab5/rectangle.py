from labs.classes.Lab5.figure import Figure

class Rectangle(Figure):
    def __init__(self):
        pass

    """
    A class representing a 3D rectangle derived from the Figure class.
    """

    def build_up_2d_line(self, color_1, color_2, symbol_1, symbol_2):
        """
        Build a line for the upper 2D section of the rectangle.

        :param color_1: The color for symbol_1.
        :param color_2: The color for symbol_2.
        :param symbol_1: The symbol for the corner.
        :param symbol_2: The symbol for the horizontal part.
        :return: The built line.
        """
        line = ''
        for size_x in range(self.size_x + 1):
            if size_x == 0 or size_x == self.size_x:
                line += self.color_line(color_1, symbol_1)
            else:
                line += self.color_line(color_2, symbol_2)
        return line

    def build_up_2d(self, lines, symbol, space_color):
        """
        Build the upper 2D section of the rectangle.

        :param lines: The lines representing the shadow.
        :param symbol: The symbol for the inclined part.
        :param space_color: The color for the space.
        :return: The built upper 2D section.
        """
        for index in range(len(lines)):
            if index == 0:
                color_1 = self._symbol_color
                color_2 = self._symbol_color
                symbol_1 = self._SYMBOLS.get('corner')
                symbol_2 = self._SYMBOLS.get('horizontal')
            else:
                color_1 = self._symbol_color
                color_2 = space_color
                symbol_1 = symbol
                symbol_2 = self._SYMBOLS.get('space')

            line = self.build_up_2d_line(color_1, color_2, symbol_1, symbol_2)

            lines[index] = lines[index] + line
        return lines

    def build_3d(self, lines):
        """
        Build the 3D section of the rectangle.

        :param lines: The lines representing the upper and lower 2D sections.
        :return: The built 3D section.
        """
        inclined_count = 1
        for index in range(len(lines)):
            line = ''
            mx = (len(lines[0]))
            shadow_mx = mx + self.size_x
            shadow = ''
            if index != 0 and index != len(lines) - 1:
                count = mx - len(lines[index]) - 1
                if index < self.size_y:
                    symbol = self._SYMBOLS.get('vertical')
                elif index == self.size_y:
                    symbol = self._SYMBOLS.get('corner')
                else:
                    count -= inclined_count
                    shadow_count = shadow_mx - len(lines[index]) - 1
                    shadow = self.build_symbol(self._SYMBOLS.get('space'), shadow_count, self._shadow_color)
                    symbol = self._SYMBOLS.get('inclined')
                    inclined_count += 1
                line = self.build_symbol(self._SYMBOLS.get('space'), count, self._color_3)
                line += self.color_line(self._symbol_color, symbol)
                line += self.color_line(self._symbol_color, shadow)
            lines[index] += line
        return lines

    def build(self):
        """
        Build the 3D rectangle.
        """
        self.set_zoom()
        shadow_up_lines = self.build_2d_shadow(self.size_z, self._SYMBOLS.get('space'), self.size_z)
        shadow_down_lines = self.build_2d_shadow(self.size_y, self._SYMBOLS.get('nothing'), self.size_z)

        up_2d = self.build_up_2d(shadow_up_lines, self._SYMBOLS.get('inclined'), self._color_1)
        down_2d = self.build_up_2d(shadow_down_lines, self._SYMBOLS.get('vertical'), self._color_2)
        down_2d += [down_2d[0]]

        lines = up_2d + down_2d
        result = self.build_3d(lines)
        self._result = self.convert(result)
