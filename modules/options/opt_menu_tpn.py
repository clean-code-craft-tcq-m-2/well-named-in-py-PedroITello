from modules.mod_test_pair_code import test_pair_to_number


class OptMenuTPN:

    def __init__(self, major_color, minor_color, test_position):
        self.major_color = major_color.capitalize()
        self.minor_color = minor_color.capitalize()
        self.test_position = test_position

    def opt_menu_tpn(self):
        if(test_pair_to_number(self.major_color.capitalize(),
                               self.minor_color.capitalize(),
                               int(self.test_position))):
            print("Tested Data:\n Major Color: "
                  + self.major_color.capitalize()
                  + " Minor Color: " + self.minor_color.capitalize()+"\n"
                  + "Test Position: " + str(self.test_position))
            print("\nTest result: Test finis correctly\n")
        else:
            print("Tested Data:\n Major Color: "
                  + self.major_color.capitalize()
                  + " Minor Color: " + self.minor_color.capitalize()+"\n"
                  + "Test Position: " + str(self.test_position))
            print("\nTest result: Test failed\n")
