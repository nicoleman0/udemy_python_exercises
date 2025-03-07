# sets
s = {1, 3, 943, 123}
3 in s # True

set({1, 2, 3}) # using set function

# for looping
for number in s:
    print(number)

# add method (doesn't add if value already in)
s = set([1, 2, 3, 4])
s.add(5)
print(s) # Output 1, 2, 3, 4, 5

# remove
s1 = {1, 2, 3, 4}
s1.remove(2)
print(s1) = {1, 3, 4}
s1.discard(3) # this is the same idea

# copy
anotherS = s1.copy()

#clear 
anotherS.clear()

# union example (set math)
math_students = ["Nick", "Henry", "Melissa", "Hugo", "Bob"]
biology_students = ["Henry", "Mark", "Sofia", "Bob"]

math_students | biology_students # or
math_students & biology_students # and
