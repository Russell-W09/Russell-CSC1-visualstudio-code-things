


"""
Importing json files ---
"""

import json

products = {}
cart = []

quit_option = "q" or "Q"

# define functions --

def menu_option():
    print("----------------------------------")
    print("Enter 1 for loading inventory:")
    print("Enter 2 for displaying ivnentory:")
    print("Enter 3 for shopping")
    print("Enter 4 for displaying cart.")
    print("Enter q or Q to quit")
    print("----------------------------------")
    print("")

def loading_inventory():
  """Load data from a JSON files"""
  try:
    with open('data/inventory.json') as file:
      data = json.load(file)
    return data
  except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading data: {e}")
    return {}

def displaying_inventory():
  # display all products in the inventory
  if not products:
    print("No inventory loaded yet. Please load inventory first.")
    return
  print("You entered 2 for displaying inventory.")
  print("\n---- Inventory ----")
  for name, details in products.items():
    print(f"{name} - ${details['price']} (Stock: {details['stock']})")
  print("---------------------")

def shopping():
  print("Welcome to shopping!")



def displaying_cart():
  print("Displaying cart")
  print("")

def invalid_option():
  print("Invalid option, please try again")
  print("")



# main code -- 

while True: 
  menu_option()
  menu_choice = input("Please enter your option here: ")
  print("")
  print("You entered the option " + str(menu_choice))
  
  if menu_choice == quit_option:
    print("Good bye")
    break
  elif menu_choice == "1":
    products = loading_inventory()
    print("You entered 1 for loading inventory")
  elif menu_choice == "2":
    displaying_inventory()
  elif menu_choice == "3":
    shopping()
  elif menu_choice == "4":
    displaying_cart()
  else:
    invalid_option()



   