from modules.mod_test_pair_code import test_pair_to_number


class OptMenuTPN:

    def opt_menu_tpn(self, major_color, minor_color, test_position):
        try:
            test_pair_to_number(major_color.capitalize(),
                                minor_color.capitalize(),
                                int(test_position))
            print("Tested Data:\n -Major Color: "
                  + major_color.capitalize()
                  + "-Minor Color: " + minor_color.capitalize()
                  + "-Test Position: " + str(test_position)+"\n")
            print("\nTest result: Test finis correctly\n")
        except AssertionError:
            print("Tested Data:\n -Major Color: "
                  + major_color.capitalize()
                  + "-Minor Color: " + minor_color.capitalize()
                  + "-Test Position: " + str(test_position)+"\n")
            print("\nTest result: Test failed\n")
