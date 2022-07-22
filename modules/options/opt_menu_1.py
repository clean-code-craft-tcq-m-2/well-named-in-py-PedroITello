from functions.pair_color_tests.init_test import test_number_to_pair
from functions.map_color_printer.printer_functions import color_map_index


def opt_menu_1(self):
    while True:
        print(color_map_index("Test Number to Pair"))
        # try:
        test_position = 2
        major_color = 'white'
        minor_color = 'blue'
        if(test_number_to_pair(int(test_position),
                               major_color.capitalize(),
                               minor_color.capitalize()
                               )):
            print("\nTest result: Test finish correctly\n")
            print("Tested Data:\nTest Position: " + str(test_position)
                  + " Major Color: " + major_color.capitalize()
                  + " Minor Color: " + minor_color.capitalize()+"\n")
            break
        else:
            print("\nTest result: Test failed\n")
            print("Tested Data:\nTest Position: " + str(test_position)
                  + " Major Color: " + major_color.capitalize()
                  + " Minor Color: " + minor_color.capitalize()+"\n")
            break
        # except Exception:
        #     message = ""
        #     message = message + "\nThis is an unaccepted position value,"
        #     message = message + "enter a valid value"
        #     print(message)
