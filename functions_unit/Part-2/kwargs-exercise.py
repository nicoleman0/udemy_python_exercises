# Assignment: Write a function called calculate that accepts a list of keyword arguments

def calculate(**kwargs):
    make_float = kwargs.get('make_float', False)
    operation = kwargs.get('operation')
    first = kwargs.get('first')
    second = kwargs.get('second')
    message = kwargs.get('message', None)
    
    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    elif operation == 'divide':
        result = first / second
    
    if make_float:
        result = float(result)

    if message:
        return message + ' ' + str(result)
    else:
        return 'The result is ' + str(result)
    
if __name__ == "__main__":
    print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"