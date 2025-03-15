from colorama import Fore
from pyfiglet import figlet_format

hello = figlet_format('Hello World!', font='doom')

text = Fore.MAGENTA + hello
print(text)