from functions.config.color_codes import MAJOR_COLORS
from functions.func_layout import (header,
                                   thematic_break,
                                   column_headers,
                                   create_columns)

map = ''


def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'


# Start render of color map
def print_color_map():
    global map
    map = map + thematic_break()
    map = map + header("3: Printable Color Map")
    map = map + thematic_break()
    map = map + header("\tMap")
    map = map + thematic_break()
    map = map + ""
    map = map + column_headers()
    map = map + thematic_break()
    for index, major_color in enumerate(MAJOR_COLORS):
        map = map + create_columns(index)
        map = map + thematic_break()
    return map
