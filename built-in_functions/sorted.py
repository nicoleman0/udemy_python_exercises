# sorted(iterable, key=None, reverse=False)
# unlike list.sort(), sorted() returns a new list and does not modify the original list.

nums = [1, 341, 28, 85, 38, 22, 19, 20]
sorted_nums = sorted(nums) # [1, 19, 20, 22, 28, 38, 85, 341]

# reverse
sorted_nums = sorted(nums, reverse=True) # [341, 85, 38, 28, 22, 20, 19, 1]

sorted_tuple = sorted((1, 2, 5, 7, 0, 3)) 

# Practical example (using key) - sorting a list of dictionaries
# sort users by their username

users = [
    {'username': 'samuel', 'tweets': ['I love cake', 'I love pie', 'hello world!']},
    {'username': 'katie', 'tweets': ['I love my cat']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo_luvr', 'tweets': ['dogs are the best', 'I\'m hungry']}
]

sorted_users = sorted(users, key=lambda user: user['username'])
print(sorted_users)

# sorting by tweet length
sorted_users = sorted(users, key=lambda user: len(user['tweets']), reverse=True)
print(sorted_users)