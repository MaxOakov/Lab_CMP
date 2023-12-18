class Figure:
    """
    Base class for creating 2D and 3D shapes with specific styles and coloring.
    """

    length_x = 0
    length_y = 0

    _result = ''
    _color_1 = '\033[44m'
    _color_2 = '\033[42m'
    _color_3 = '\033[43m'

    _default_color = '\033[00m'
    _shadow_color = '\033[47m'
    _symbol_color = '\033[36m'

    _space = 0
    _zoom = 1

    size_x = None
    size_y = None
    size_z = None

    _COLORS = {
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'WHITE': '\033[37m',
    }

    _SYMBOLS = {
        'corner': '+',
        'horizontal': '—',
        'vertical': '|',
        'inclined': '/',
        'space': ' ',
        'nothing': '',
    }

    def __init__(self, **kwargs):
        """
        Initialize the Figure.

        :param kwargs: Keyword arguments for setting size_x, size_y, and size_z.
        """
        if 'size_y' in kwargs:
            self.size_y = kwargs['size_y']
        if 'size_x' in kwargs:
            self.size_x = kwargs['size_x']
        if 'size_z' in kwargs:
            self.size_z = kwargs['size_z']
        if self.size_x:
            if not self.size_y or not self.size_z:
                self.size_y = self.size_z = self.size_x
            self.set_length_x()
            self.set_length_y()
        else:
            self.size_y = self.size_z = self.size_x = 0

    def set_length_x(self):
        """Set the length_x attribute."""
        self.length_x = self.size_x

    def set_length_y(self):
        """Set the length_y attribute."""
        self.length_y = self.size_y

    def set_zoom(self):
        """Set the zoom level for size_x, size_y, and size_z."""
        self.size_x *= self._zoom
        self.size_y *= self._zoom
        self.size_z *= self._zoom

    def color_line(self, color, line):
        """
        Apply color to a line.

        :param color: Color code.
        :param line: Line to be colored.
        :return: Colored line.
        """
        return color + line + self._default_color

    def build_2d_shadow(self, count, symbol, size):
        """
        Build a 2D shadow effect.

        :param count: Number of shadow lines.
        :param symbol: Symbol for the shadow.
        :param size: Size of the shadow.
        :return: List of shadow lines.
        """
        lines = []
        for index in range(count):
            line = self.build_symbol(self._SYMBOLS.get('space'), self._space, self._default_color)
            line += self.color_line(self._default_color, symbol * (size - index))
            lines += [line]
        return lines

    def build_symbol(self, symbol, count, color):
        """
        Build a line of symbols.

        :param symbol: Symbol to be repeated.
        :param count: Number of times to repeat the symbol.
        :param color: Color code.
        :return: Line of symbols.
        """
        line = ''
        for i in range(count):
            line += self.color_line(color, symbol)
        return line

    def build(self):
        """Build the figure."""
        # Your logic for building the shape

    def create(self):
        """Create the figure."""
        self.set_zoom()
        self.build()

    def save(self, filename):
        """
        Save the figure to a file.

        :param filename: Name of the file.
        """
        self.create()
        result = self.remove_color_codes(self._result)
        with open(filename, 'w') as file:
            file.write(result)

    def remove_color_codes(self, text):
        """
        Remove color codes from a text.

        :param text: Text with color codes.
        :return: Text without color codes.
        """
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end + 1:]
            else:
                break
        return text

    def convert(self, lines):
        """
        Convert a list of lines to a string.

        :param lines: List of lines.
        :return: String representation of the lines.
        """
        return '\n'.join(lines)

    def __str__(self):
        """
        Get a string representation of the figure.

        :return: String representation.
        """
        return self._result
