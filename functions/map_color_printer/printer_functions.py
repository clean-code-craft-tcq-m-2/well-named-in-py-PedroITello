from functions.config.color_codes import MAJOR_COLORS, MINOR_COLORS
from functions.func_layout import header, thematic_break

triple_tab = "\t\t\t"


def color_map_index(message):
    index_string = ""
    index_string = index_string + thematic_break()
    index_string = index_string + header(message)
    index_string = index_string + thematic_break()
    index_string = index_string + ("Major Colors"
                                   + triple_tab
                                   + "Minor Colors"
                                   + "\n\n")
    for index, major_color in enumerate(MAJOR_COLORS):
        index_string = index_string + (major_color
                                       + triple_tab
                                       + MINOR_COLORS[index]
                                       + "\n")
    index_string = index_string + "\nPair number range: (1-25)\n"
    index_string = index_string + thematic_break()
    return index_string
