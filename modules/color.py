from termcolor import colored

test_script = colored(text="This is officially a test script.", color="cyan", on_color="on_magenta", attrs=["blink"])
print(test_script)

name = colored(text="Nicholas", on_color="on_red", attrs= ["blink"])
print(name)