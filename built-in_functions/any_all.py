# all - returns True if all elements of the iterable are true (or if the iterable is empty)
# List comprehension brackets are not necessary, but they make the code more readable
# If the iterable is empty, the function returns True

all([0, 1, 2, 3]) # False - 0 is False
all([char for char in 'eio' if char in 'aeiou']) # True - all characters are vowels
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]) # True - all numbers are even

# all - practical example

people = ['Nick', 'Jeremy', 'Charles', 'Amy', 'Arnold']
all([name[0] == 'A' for name in people]) # False - not all names start with 'A'

nums = [2, 4, 6, 8, 10]
all([num % 2 == 0 for num in nums])

# any - returns True if any element of the iterable is true. If the iterable is empty, returns False

any([val for val in [1, 2, 3, 4] if val > 2]) # True - at least one value is greater than 2

nums2 = [1, 3, 4, 5, 7, 10, 19, 27]
any([num for num in nums2 if num % 2 != 0]) # True - at least one number is odd