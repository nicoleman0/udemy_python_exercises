from pyfiglet import figlet_format
from termcolor import colored

msg = input("What would you like to print out?\n")
color = input("What color would you like to choose?\n")

ascii_art = figlet_format(msg)
colored_ascii = colored(ascii_art, color=color.lower())

print(colored_ascii)