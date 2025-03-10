# Default parameters

def exponent(num, power=2): # power is optional and defaults to 2
    return num ** power

print(exponent(9))  # 81

def add(a=10, b=20): # a and b are optional and default to 10 and 20
    return a + b

print(add()) # 30