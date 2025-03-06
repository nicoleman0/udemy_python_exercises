# list comprehension method

numbers = [1,2,3,4,5,6,7,8,9]

squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)

# another example

name = 'nick'

new_name = [char.upper() for char in name]

print(new_name)

# bad/slow method

numbers = [1,2,3,4,5,6,7,8,9]
squared_numbers = []

for num in numbers:
    squared_num = num ** 2
    squared_numbers.append(squared_num)

print(squared_numbers)
