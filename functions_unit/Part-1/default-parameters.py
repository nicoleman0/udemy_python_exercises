# Default parameters are used when a parameter is not provided by the caller
# Using = when defining a function allows us to set a default value for a parameter

# Example
def exponent(num, power=2): # power is optional and defaults to 2
    return num ** power

print(exponent(9))  # 81

def add(a=10, b=20): # a and b are optional and default to 10 and 20
    return a + b

print(add()) # 30

# Default parameters can be used with any type of parameter, not just numbers
# Example: Using default parameters with a function
def math(a, b, fn=add): # fn is optional and defaults to the add function
    return fn(a, b)

print(math(10, 20)) # 30
print(math(30, 20, exponent)) # 900