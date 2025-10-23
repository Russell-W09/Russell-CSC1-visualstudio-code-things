
# nothing different from slide 3

def menu_option():
    print("----------------------------------")
    print("Enter 1 for loading inventory:")
    print("Enter 2 for displaying ivnentory:")
    print("Enter 3 for shopping")
    print("Enter 4 for displaying cart.")
    print("Enter q or Q to quit")
    print("----------------------------------")
    print("")

quit_option = "q" or "Q"

while True: 
  menu_option()
  menu_choice = input("Please enter your option here: ")
  print("")
  print("You entered the option " + str(menu_choice))
  
  if menu_choice == quit_option:
    print("Good bye")
    break
  elif menu_choice == "1":
    print("Loading inventory")
    print("")
  elif menu_choice == "2":
    print("Displaying inventory")
    print("")
  elif menu_choice == "3":
    print("Shopping")
    print("")
  elif menu_choice == "4":
    print("Displaying cart")
    print("")
  else:
    print("Invalid option, please try again")
    print("")


   