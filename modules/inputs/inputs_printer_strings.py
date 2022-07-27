from functions.config.color_codes import MAJOR_COLORS, MINOR_COLORS

sep1 = "\t |\t"
sep2 = "\t\t|\t"
sep3 = "\t\t|\t\n"


def construct_full_string(index, major_color):
    string = ("   " + str((index + 1) + (5 * major_color)) + sep1
              + MAJOR_COLORS[major_color] + sep2
              + MINOR_COLORS[index] + sep3)
    return string


def construct_simple_string(index, major_color):
    string = ("   " + str((index + 1) + (5 * major_color)) + sep1
              + " " + sep2
              + MINOR_COLORS[index] + sep3)
    return string
