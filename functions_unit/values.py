# Default parameters

def exponent(num, power=2): # power is optional and defaults to 2
    return num ** power

print(exponent(9))  # 81

def add(a=10, b=20): # a and b are optional and default to 10 and 20
    return a + b

print(add()) # 30

# Example: Using default parameters with a function
def math(a, b, fn=add): # fn is optional and defaults to the add function
    return fn(a, b)

print(math(10, 20)) # 30
print(math(30, 20, exponent)) # 900