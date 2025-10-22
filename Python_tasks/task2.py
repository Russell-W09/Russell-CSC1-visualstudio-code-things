
# using funtions early 

def menu_option():
    print("----------------------------------")
    print("Enter 1 for loading inventory:")
    print("Enter 2 for displaying ivnentory:")
    print("Enter 3 for shopping")
    print("Enter 4 for displaying cart.")
    print("Enter q or Q to quit")
    print("----------------------------------")

menu_option()
menu_choice = input("Please enter your option here: ")
print("You entered the option " + str(menu_choice))

