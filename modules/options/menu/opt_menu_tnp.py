from modules.mod_test_pair_code import test_number_to_pair


# Evaluate Tes Number to Pair
class OptMenuTNP:

    def opt_menu_tnp(self, test_position, major_color, minor_color):
        try:
            test_number_to_pair(int(test_position),
                                major_color.capitalize(),
                                minor_color.capitalize())
            print("Tested Data:\n-Test Position: " + str(test_position)
                  + " -Major Color: " + major_color.capitalize()
                  + " -Minor Color: " + minor_color.capitalize())
            print("\nTest result: Test finish correctly\n")
        except AssertionError:
            print("Tested Data:\n-Test Position: " + str(test_position)
                  + " -Major Color: " + major_color.capitalize()
                  + " -Minor Color: " + minor_color.capitalize())
            print("\nTest result: Test failed\n")
