# clear
d = dict(a=1, b=2, c=3, d=4)
d.clear()
print(d)  # Output: {}

# copy (makes a clone assigned to variable)
d = dict(a=1, b=2, c=3, d=4)
d_copy = d.copy()
print(d_copy)

# fromkeys
new_dict = {}.fromkeys(["email"], "unknown")
print(new_dict) # Output {'email': 'unknown'}

# another fromkeys example (easy way to create a new dict)
new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "N/A")
print(new_user)

# get
d = dict(a=1, b=2, c=3, d=4)
d = d.get("a")
print(d) # Output: 1
d = d.get("no_key")
print(d) # Output: None
