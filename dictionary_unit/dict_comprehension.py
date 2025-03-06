# dictionary comprehension

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key, value in numbers.items()} # key is same, value squared
print(squared_numbers) # Output: {'first': 1, 'second': 4, 'third': 9}

# another example
numbers_2 = {num: num ** 2 for num in [1, 2, 3, 4, 5]} # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(numbers_2)

# example 3
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)

# example 4
user_info = {"name": "nick", "age": "24", "city": "NYC"}
capital_user_info = {k.upper(): v.upper() for k, v in user_info.items()}
print(capital_user_info) # Output: {'NAME': 'NICK', 'AGE': 24, 'CITY': 'NYC'

# example 5 (two lists)
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(len(list1))}
print(answer) # Output: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
dict(zip(list1,list2)) # this is the easy version
