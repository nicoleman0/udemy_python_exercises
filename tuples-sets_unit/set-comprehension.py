example = {x ** 2 for x in range(10)} # set 
print(example) # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81})

dictionary = {x:x ** 2 for x in range(10)}

# example
string = "hello"
vowels = len({char for char in string if char in 'aeiou'}) == 5 # this checks if string has all five vowels

if vowels:
    print(True)
else:
    print(False)
