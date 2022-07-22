from color_codes import MAJOR_COLORS, MINOR_COLORS
from pair_color_tests import test_number_to_pair, test_pair_to_number
from print_color_map import print_color_map, color_map_index
import os
import sys

def menu():
  print("\n************ Welcome to Map Color Application **************")
  print()

  choice = input("""
                1: Test Number to Pair
                2: Test Pair to Number
                3: Print Color Map
                4: Exit

                Please enter your choice: """)

  if choice == "1":
    while True:
      print(color_map_index())
      try:
        test_position = int(input("Insert Pair Number: "))
        major_color = str(input ("Insert Major Color: "))
        minor_color = input ("Insert Minor Color: ")
        if(test_number_to_pair(int(test_position),major_color.capitalize(), minor_color.capitalize())):
          print("\nTest result: Test finis correctly\n")
          menu()
          break
        else:
          print("\nTest result: Test failed\n")
          menu()
          break
      except:
        print("\nThis is an unaccepted inputs, enter a valid values")
  elif choice == "2":
    while True:
      print(color_map_index())
      major_color = str(input ("Insert Major Color: "))
      minor_color = input ("Insert Minor Color: ")
      try:
        test_position = int(input("Insert Pair Number: "))
        if(test_pair_to_number(major_color.capitalize(), minor_color.capitalize(), int(test_position))):
          print("\nTest result: Test finis correctly\n")
          menu()
          break
        else:
          print("\nTest result: Test failed\n")
          menu()
          break
      except:
        print("\nThis is an unaccepted inputs, enter a valid values")
      test_pair_to_number('Violet', 'Slate', 25)
  elif choice == "3":
      print(print_color_map())
      original_stdout = sys.stdout
      with open('color_map.txt', 'w') as file:
        sys.stdout = file
        print(print_color_map())
        sys.stdout = original_stdout
        print("\nFile saved as: "+ os.getcwd() + "\\" + file.name)
      menu()
  elif choice ==  "4":
      print("Done :)")
      sys.exit
  else:
      print("You must only select option between 1 - 4")
      print("Please try again")
      menu()

if __name__ == '__main__':
  menu()