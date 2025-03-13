# abs - returns the absolute value of a number
# abs(x) - x can be an integer or a float

abs(-7.25) # 7.25
abs(7.25) # 7.25
abs(0) # 0

# sum() - returns the sum of all items in an iterable (list, tuple, etc.)
# sum(iterable, start) - start is optional, default is 0

sum([1, 2, 3]) # 6
sum([1, 2, 3], 10) # 16
sum((1.4, 2.7, 3.8)) # 7.9

# you can't use sum for strings

''.join(['hello', 'world']) # 'helloworld'

# round() - rounds a number to a specified number of decimal places
# round(number, digits) - digits is optional, default is 0

round(3.1432, 2) # 3.14
round(3.1432) # 3