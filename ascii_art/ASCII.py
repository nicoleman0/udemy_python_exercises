from pyfiglet import figlet_format
from termcolor import colored

def print_artwork(msg, color, font):
    """
    Prints out a colorized ASCII styled message with the font of your choice.
    """
    
    legit_colors = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_grey', 'dark_grey', 'light_red', 
 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan')
    
    legit_fonts = ('doom', 'standard', 'slant')
    
    if color.lower() not in legit_colors:
        color = 'blue'
    if font not in legit_fonts:
        font = 'standard'

    ascii_art = figlet_format(msg, font=font.lower())
    colored_ascii = colored(ascii_art, color=color.lower())
    print(colored_ascii)

msg = input("What would you like to print out?\n")
color = input("What color would you like to choose?\n")
font = input("What font would you like to use?\n")

print_artwork(msg, color, font)