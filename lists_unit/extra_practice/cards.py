# try to use list comprehension in this game

from random import randint

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def pick_card():
    """picks a random card from the deck"""
    return cards[randint(0, len(cards) - 1)] # generates random int that represents index

# beginning of game

computer_card = pick_card()

print("This is a card game. First, you must pick a card. Good luck!")

y_or_n = input("Would you like to pick a card? (y/n): ").lower()

if y_or_n[0] == "y":
    player_card = pick_card()
    print(f"You picked {player_card}.")
else:
    print("OK bye.")
    exit()

if computer_card == player_card:
       print("You guys have the same cards! Tie game...")