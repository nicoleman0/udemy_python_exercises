# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# code
if food in bakery_stock:
    print(f"There is {bakery_stock[food]} {food} left.") # this uses the food choice and outputs its value
else:
    print("We don't make that.")