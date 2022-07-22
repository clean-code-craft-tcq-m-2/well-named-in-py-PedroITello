from modules.options.opt_menu_tnp import OptMenuTNP
from modules.options.opt_menu_tpn import OptMenuTPN
from modules.options.opt_menu_print import OptMenuPrint
from functions.map_color_printer.printer_functions import color_map_index
import sys


class InputsMenu:

    def __init__(self, choice):
        self.choice = str(choice)

    def choice_selector(self):
        if self.choice == "1":
            print(color_map_index("1: Test Number to Pair"))
            OptMenu = OptMenuTNP("5", "red", "green")
            OptMenu.opt_menu_tnp()
            OptMenu = OptMenuTNP("18", "yellow", "green")
            OptMenu.opt_menu_tnp()
        elif self.choice == "2":
            print(color_map_index("2: Test Pair to Number"))
            OptMenu = OptMenuTPN("black", "greem", "13")
            OptMenu.opt_menu_tpn()
            OptMenu = OptMenuTPN("red", "brown", "5")
            OptMenu.opt_menu_tpn()
        elif self.choice == "3":
            OptMenuPrint().opt_menu_print()
        elif self.choice == "4":
            print("\n4: Done :)")
            sys.exit
        else:
            print("You must only select option between"
                  + "1 - 4\nPlease try again")
            self.menu()
