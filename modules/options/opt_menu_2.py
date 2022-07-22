from functions.pair_color_tests.init_test import test_pair_to_number
from functions.map_color_printer.printer_functions import color_map_index


def opt_menu_2(self):
    while True:
        print(color_map_index())
        try:
            major_color = 'white'
            minor_color = 'blue'
            # major_color = str(input("Insert Major Color: "))
            # minor_color = str(input("Insert Minor Color: "))
            try:
                test_position = 1
                # test_position = int(input("Insert Pair Number: "))
                if(test_pair_to_number(major_color.capitalize(),
                                       minor_color.capitalize(),
                                       int(test_position))):
                    print("\nTest result: Test finis correctly\n")
                    # self.menu()
                    break
                else:
                    print("\nTest result: Test failed\n")
                    # self.menu()
                    break
            except Exception:
                message = ""
                message = message + "\nThis is an unaccepted position value,"
                message = message + "enter a valid value"
                print(message)
        except Exception:
            print("\nTest result: Test failed\n")
            # self.menu()
            break
