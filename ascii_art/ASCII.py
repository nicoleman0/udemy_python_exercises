from pyfiglet import figlet_format
from termcolor import colored

def print_artwork(msg, color):
    legit_colors = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey', 'dark_grey', 'light_red', 
 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan')
    if color.lower() not in legit_colors:
        color = 'blue'

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color.lower())
    print(colored_ascii)

msg = input("What would you like to print out?\n")
color = input("What color would you like to choose?\n")

print_artwork(msg, color)