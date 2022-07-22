from color_codes import MAJOR_COLORS, MINOR_COLORS
import string

map = ''
column_separator = "\t\t|\t"
column_end = "\t\t|\t\n"
triple_tab = "\t\t\t"

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def color_map_index():
    index_string = ""
    index_string = index_string + thematic_break()
    index_string = index_string + header("\tOptions Help")
    index_string = index_string + thematic_break()
    index_string = index_string + ("Major Colors"
    + triple_tab
    +"Minor Colors"
    +"\n\n")
    for index,major_color in enumerate(MAJOR_COLORS):
        index_string = index_string + (major_color
                        +triple_tab
                        +MINOR_COLORS[index]
                        +"\n")
    index_string = index_string + "\nPair number range: (1-25)\n"
    index_string = index_string + thematic_break()
    return index_string

# Generate line to separate topics in print view form
def thematic_break():
    line = '';
    for i in range(56):
        line = line + "_"
        if(i==55):
            line = line + '\n'
    return line

# Create headers in form
def header(string):
    return "\n\t\t"+string+"\n"

def column_headers():
    return " ".join(["Pair No. |","\tMAJOR COLOR\t|","\tMINOR COLOR\t|\n"])

# Generate spaces for any color map configuration
def create_columns(major_color):
    generated_columns=""
    for index,minor_color in enumerate(MINOR_COLORS):
        if(index==2):
            generated_columns = generated_columns + (
            "   "+str((index+1)+(5*major_color))
            +"\t |\t"
            +MAJOR_COLORS[major_color]
            +column_separator
            +MINOR_COLORS[index]
            +column_end)
        else:
            generated_columns = generated_columns + (
            "   "+str((index+1)+(5*major_color))
            +"\t |\t"
            +""
            +column_separator
            +MINOR_COLORS[index]
            +column_end)
    return generated_columns
# Start render of color map
def print_color_map():
    global map,arrow
    map = map + header("Printable Color Map")
    map = map + thematic_break()
    map = map + header("\tMap")
    map = map + thematic_break()
    map = map + ""
    map = map + column_headers()
    map = map + thematic_break()
    for index,major_color in enumerate(MAJOR_COLORS):
        map = map + create_columns(index)
        map = map + thematic_break()
    return map

