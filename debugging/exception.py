# raising your own exceptions

def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta', 'red', 'white')
    if type(color) is not str:
        raise TypeError('color must be a string')
    if type(text) is not str:
        raise TypeError('text must be a string')
    if color not in colors:
        raise ValueError(f'color must be one of {colors}')
    
    print(f"You chose {color} color for {text}")


colorize('hello', 'black') # ValueError
colorize('hello', 83) # TypeError
