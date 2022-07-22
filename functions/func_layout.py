from functions.config.color_codes import MINOR_COLORS
from modules.inputs.inputs_printer_strings import (construct_full_string,
                                                   construct_simple_string)


# Generate line to separate topics in print view form
def thematic_break():
    line = ''
    for i in range(56):
        line = line + "_"
        if(i == 55):
            line = line + '\n'
    return line


# Create headers in form
def header(string):
    return "\n\t\t" + string + "\n"


def column_headers():
    return " ".join(["Pair No. |", "\tMAJOR COLOR\t|", "\tMINOR COLOR\t|\n"])


# Generate spaces for any color map configuration
def create_columns(major_color):
    generated_columns = ""
    for index, minor_color in enumerate(MINOR_COLORS):
        if(index == 2):
            temp = construct_full_string(index, major_color)
            generated_columns = generated_columns + temp
        else:
            temp = construct_simple_string(index, major_color)
            generated_columns = generated_columns + temp
    return generated_columns
