from modules.inputs.inputs_menu import choice_selector
# from modules.inputs.inputs_printer import thematic_break, header


class Menu:

    def menu(self):
        # print(thematic_break())
        # print(header("Option Menu"))
        # print(thematic_break())
        choice_selector(self, "1")
        choice_selector(self, "2")
        choice_selector(self, "3")
        choice_selector(self, "4")
        # choice = input("""
        #         1: Test Number to Pair
        #         2: Test Pair to Number
        #         3: Print Color Map
        #         4: Exit

        #         Please enter your choice: """)
