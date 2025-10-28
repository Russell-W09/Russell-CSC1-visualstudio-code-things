
import json

products = {}
cart = []

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
  print("You entered 2 for displaying inventory.")
  print("--------")
  for name, details in products.items():
    print(f"{name}) - ${details['price']}")
  print("--------")

def shopping():
  print("Welcome to shopping!")