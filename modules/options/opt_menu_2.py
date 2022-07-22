from functions.pair_color_tests.init_test import test_pair_to_number
from functions.map_color_printer.printer_functions import color_map_index

def opt_menu_2(self):
    while True:
        print(color_map_index())
        major_color = str(input ("Insert Major Color: "))
        minor_color = input ("Insert Minor Color: ")
        try:
            test_position = int(input("Insert Pair Number: "))
            if(test_pair_to_number(major_color.capitalize(), minor_color.capitalize(), int(test_position))):
                print("\nTest result: Test finis correctly\n")
                self.menu()
                break
            else:
                print("\nTest result: Test failed\n")
                self.menu()
                break
        except:
            print("\nThis is an unaccepted inputs, enter a valid values")
        test_pair_to_number('Violet', 'Slate', 25)