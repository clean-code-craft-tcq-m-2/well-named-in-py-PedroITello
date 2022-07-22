from modules.mod_test_pair_code import test_number_to_pair


# Evaluate Tes Number to Pair
class OptMenuTNP:

    def __init__(self, test_position, major_color, minor_color):
        self.test_position = test_position
        self.major_color = major_color.capitalize()
        self.minor_color = minor_color.capitalize()

    def opt_menu_tnp(self):
        if(test_number_to_pair(int(self.test_position),
                               self.major_color,
                               self.minor_color
                               )):
            print("Tested Data:\n-Test Position: " + str(self.test_position)
                  + " -Major Color: " + self.major_color
                  + " -Minor Color: " + self.minor_color)
            print("\nTest result: Test finish correctly\n")
        else:
            print("Tested Data:\n-Test Position: " + str(self.test_position)
                  + " -Major Color: " + self.major_color
                  + " -Minor Color: " + self.minor_color)
            print("\nTest result: Test failed\n")
