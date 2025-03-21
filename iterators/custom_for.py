# custom for loop example

def myfor(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)


def square(x):
    print(x**2)


myfor(range(10), square)
