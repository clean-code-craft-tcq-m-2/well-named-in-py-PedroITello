from color_codes import MAJOR_COLORS, MINOR_COLORS

def _get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS):
    raise Exception('Minor index out of range')
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def _get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MINOR_COLORS) + minor_index + 1


def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = _get_color_from_pair_number(pair_number)
  if(major_color == expected_major_color):
    if(minor_color == expected_minor_color):
        return True
    else:
        return False
  else:
    return False



def test_pair_to_number(major_color, minor_color, expected_pair_number):
  try:
    pair_number = _get_pair_number_from_color(major_color, minor_color)
    if(pair_number == expected_pair_number):
        return True
    else:
        return False
  except:
      return False
