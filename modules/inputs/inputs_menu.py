from modules.options.opt_menu import MenuOptions
from functions.map_color_printer.printer_functions import color_map_index
import sys


class InputsMenu(MenuOptions):

    def __init__(self):
        self.menuOptions = MenuOptions()

    def choice_selector(self, choice):
        if choice == "1":
            print(color_map_index("1: Test Number to Pair"))
            self.menuOptions.opt_menu_tnp("5", "red", "green")
            self.menuOptions.opt_menu_tnp("18", "yellow", "green")
            self.menuOptions.opt_menu_tnp("1", "white", "blue")
        elif choice == "2":
            print(color_map_index("2: Test Pair to Number"))
            self.menuOptions.opt_menu_tpn("black", "green", "13")
            self.menuOptions.opt_menu_tpn("red", "brown", "5")
            self.menuOptions.opt_menu_tpn("white", "blue", "3")
        elif choice == "3":
            self.menuOptions.opt_menu_print()
        elif choice == "4":
            print("\n4: Done :)")
            sys.exit
        else:
            print("\nYou must only select option between"
                  + "1 - 4\nPlease try again\n")
