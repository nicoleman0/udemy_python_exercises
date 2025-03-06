# pop (removes key/value pair from dict)
# then pop returns corresponding value to the removed key
d = dict(a=1, b=2, c=3)
d.pop("a") # Output: 1
print(d) # Output: {'b': 2, 'c': 3}

# popitem (removes a random key/value tuple in a dict)
c = dict(a=1, b=2, c=3, d=4, e=5, f=6)
c.popitem()
print(c) 

# update (adds values/overwrites values already there)
first = dict(a=1, b=2, c=3)
second = dict(d=4, e=5, f=6)
first.update(second)
print(first) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

