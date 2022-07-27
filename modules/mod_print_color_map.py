from functions.config.color_codes import MAJOR_COLORS
from functions.func_layout import (header,
                                   thematic_break,
                                   column_headers,
                                   create_columns)


class PrintColorMap:

    def __init__(self):
        self.map = ""

    def color_pair_to_string(major_color, minor_color):
        return f'{major_color} {minor_color}'

    # Start render of color map
    def print_color_map(self):

        self.map = self.map + thematic_break()
        self.map = self.map + header("3: Printable Color Map")
        self.map = self.map + thematic_break()
        self.map = self.map + header("\tMap")
        self.map = self.map + thematic_break()
        self.map = self.map + ""
        self.map = self.map + column_headers()
        self.map = self.map + thematic_break()
        for index, major_color in enumerate(MAJOR_COLORS):
            self.map = self.map + create_columns(index)
            self.map = self.map + thematic_break()
        return self.map
