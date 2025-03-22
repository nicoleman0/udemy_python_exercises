# we can pass funcs as args to other funcs
# these are all higher order functions
from random import choice


def sum(n, func):
    total = 0
    for num in range(1, n+1):   # skips zero
        total += func(num)
    return total


def square(num):
    return num * num


def cube(num):
    return num * num * num


s = sum(4, square)
print(s)

# nested function


def greet(person):
    def get_message():
        return "Hello "

    result = get_message() + person
    return result


print(greet("Nick"))

# returning a func


def make_laugh():
    def get_laugh():
        l = choice(('Hahahah', 'hehehehe', 'muahahahaha'))
        return l

    return get_laugh


laugh = make_laugh()
print(laugh())
