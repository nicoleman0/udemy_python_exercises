# iterating over a dict
first_dictionary = {
    "name": "Nick",
    "age": 24,
    "city": "New York",
    "pets": "Franky",
    "hobbies": ["coding", "reading", "cooking", "40k"],
    "is_cool": True
}

# values
for value in first_dictionary.values():
    print(value)

# keys
for key in first_dictionary.keys():
    print(key)

# items
for key, value in first_dictionary.items():
    print(f"The key is {key}, and the value is {value}.")

# to check if a dict has a key
if "favorite_food" in first_dictionary:
    print("That key is in the dictionary.")
else:
    print("That key is not in the dictionary.")

# for values
"Franky" in first_dictionary.values()