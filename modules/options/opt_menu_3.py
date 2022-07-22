from modules.mod_print_color_map import print_color_map
import sys
import os


def opt_menu_3(self):
    while True:
        print(print_color_map())
        original_stdout = sys.stdout
        with open('color_map.txt', 'w') as file:
            sys.stdout = file
            print(print_color_map())
            sys.stdout = original_stdout
            print("\nFile saved as: " + os.getcwd() + "\\" + file.name)
            # self.menu()
            break
