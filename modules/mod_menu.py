from modules.inputs.inputs_menu import InputsMenu
from functions.func_layout import thematic_break, header


class Menu:

    def menu(self):
        print(thematic_break())
        print(header("Option Menu"))
        print(thematic_break())
        print(header("Functionality Test"))
        print("""
        #         1: Test Number to Pair
        #         2: Test Pair to Number
        #         3: Print Color Map
        #         4: Exit
        #

        Functionality test beggins now...""")
        for i in range(4):
            input = InputsMenu(i+1)
            input.choice_selector()
