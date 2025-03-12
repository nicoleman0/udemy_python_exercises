users = [
 {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
 {"username": "katie", "tweets": ["I love my cat"]},
 {"username": "jeff", "tweets": []},
 {"username": "bob123", "tweets": []},
 {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
 {"username": "guitar_gal", "tweets": []}
 ]

# Extract inactive users using filter
inactiveUsers = list(filter(lambda user: not user["tweets"], users))

# list comprehension method (better-looking/easier)
inactiveUsers2 = [user for user in users if not user["tweets"]]

# Extract usernames using map and filter
usernames = list(map(lambda user: user["username"].upper(), 
                     filter(lambda u: not u['tweets'], users))) # ['JEFF', 'BOB123', 'GUITAR_GAL']

# list comprehension method (better-looking/easier)

usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

# Combining filter and map
# part one is the function, part two is the iterable 
# filter runs first, then map runs on the result of filter

names = ['Lassie', 'Colt', 'Rusty']
list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) > 5, names)))

# list comprehension method (better-looking/easier)
[f"Your instructor is {name}" for name in names if len(name) < 5] # ['Your instructor is Colt']
