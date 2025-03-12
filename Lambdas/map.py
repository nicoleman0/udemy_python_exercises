# Map function is used to apply a function to all the elements of specified iterable and return map object.
# Syntax: map(function, iterable)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
doubles = list(map(lambda x: x * 2, nums))

people = ['John', 'Mike', 'Sarah', 'Sally']
upper = list(map(lambda name: name.upper(), people))

if __name__ == '__main__':
    print(doubles)
    print(upper)

# Example 2 - Extracting first names from a list of dictionaries

names = [{'first': 'John', 'last': 'Doe'}, {'first': 'Mike', 'last': 'Smith'}, {'first': 'Sarah', 'last': 'Connor'}]

first_names = list(map(lambda x: x['first'], names))

if __name__ == '__main__':
    print(first_names)

# Example 3 - Decrement all the elements of a list by 1

def decrement_list(num_list):
    return list(map(lambda x: x-1, num_list))