from functions.pair_color_tests.init_test import test_number_to_pair
from functions.map_color_printer.printer_functions import color_map_index


def opt_menu_1(self):
    while True:
        print(color_map_index())
        try:
            test_position = int(input("Insert Pair Number: "))
            major_color = str(input("Insert Major Color: "))
            minor_color = input("Insert Minor Color: ")
            if(test_number_to_pair(
                int(test_position),
                major_color.capitalize(),
                minor_color.capitalize()
            )):
                print("\nTest result: Test finis correctly\n")
                self.menu()
                break
            else:
                print("\nTest result: Test failed\n")
                self.menu()
                break
        except Exception:
            message = message + "\nThis is an unaccepted test position value,"
            message = message + "enter a valid value"
            print(message)
