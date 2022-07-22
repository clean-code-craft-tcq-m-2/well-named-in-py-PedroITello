from functions.config.color_codes import MAJOR_COLORS, MINOR_COLORS


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
        full_string = (
            "   " + str((index + 1) + (5 * major_color))
            + "\t |\t" + MAJOR_COLORS[major_color] + "\t\t|\t"
            + MINOR_COLORS[index] + "\t\t|\t\n")
        simple_string = (
            "   " + str((index + 1) + (5 * major_color))
            + "\t |\t" + " " + "\t\t|\t"
            + MINOR_COLORS[index] + "\t\t|\t\n")
        if(index == 2):
            generated_columns = generated_columns + full_string
        else:
            generated_columns = generated_columns + simple_string
    return generated_columns
