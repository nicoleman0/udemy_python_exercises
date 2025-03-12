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
print(inactiveUsers)