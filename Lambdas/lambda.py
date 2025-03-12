# example function
def square(num): return num * num

# lambda functions
# lambda is like a function but it is not defined with any name
square2 = lambda num: num * num 

add = lambda a, b: a + b

if __name__ == '__main__':
    print(square2(5))
    print(add(5, 10))

# more examples
multiply = lambda x, y: x * y

if __name__ == '__main__':
    print(multiply(5, 10))

# Cube
cube = lambda x: x ** 3