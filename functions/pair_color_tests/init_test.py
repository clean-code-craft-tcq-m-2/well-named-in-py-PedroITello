from functions.pair_color_tests.tests_functions import get_color_from_pair_number, get_pair_number_from_color

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  if(major_color == expected_major_color):
    if(minor_color == expected_minor_color):
        return True
    else:
        return False
  else:
    return False



def test_pair_to_number(major_color, minor_color, expected_pair_number):
  try:
    pair_number = get_pair_number_from_color(major_color, minor_color)
    if(pair_number == expected_pair_number):
        return True
    else:
        return False
  except:
      return False