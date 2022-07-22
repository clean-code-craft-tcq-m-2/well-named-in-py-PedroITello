from modules.options.opt_menu_1 import opt_menu_1
from modules.options.opt_menu_2 import opt_menu_2
from modules.options.opt_menu_3 import opt_menu_3
import sys


def choice_selector(self, choice):
    if choice == "1":
        opt_menu_1(self)
    elif choice == "2":
        opt_menu_2(self)
    elif choice == "3":
        opt_menu_3(self)
    elif choice == "4":
        print("Done :)")
        sys.exit
    else:
        print("You must only select option between 1 - 4")
        print("Please try again")
        self.menu()
