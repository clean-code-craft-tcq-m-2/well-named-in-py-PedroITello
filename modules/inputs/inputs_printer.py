from functions.config.color_codes import MAJOR_COLORS, MINOR_COLORS

column_separator = "\t\t|\t"
column_end = "\t\t|\t\n"


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
        aux_string = ""
        if(index == 2):
            aux_string = "   " + str((index+1)+(5*major_color))
            + "\t |\t" + MAJOR_COLORS[major_color] + column_separator
            + MINOR_COLORS[index]+column_end
            generated_columns = generated_columns + aux_string
        else:
            aux_string = "   " + str((index+1)+(5*major_color))
            + "\t |\t" + "" + column_separator
            + MINOR_COLORS[index] + column_end
            generated_columns = generated_columns + aux_string
    return generated_columns
