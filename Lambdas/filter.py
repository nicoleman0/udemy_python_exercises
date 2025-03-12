# Filter function, used to filter out elements from a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter must contain a function that returns a boolean value
# The function is applied to each element in the list
# If the function returns True, the element is kept

evens = list(filter(lambda x: x % 2 == 0, l)) # [2, 4, 6, 8, 10]

# Filter can also be used to filter out elements from a list of strings

names = ['Alice', 'Bob', 'Charlie', 'Alex', 'Alexandra']

a = list(filter(lambda name: name.startswith('A'), names)) # ['Alice', 'Alex', 'Alexandra']

# another method
a_names = list(filter(lambda n: n[0] == 'A', names)) # ['Alice', 'Alex', 'Alexandra']