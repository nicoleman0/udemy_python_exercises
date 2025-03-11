# unpacking lists and tuples with * operator
def sum_all_values(*args):
   total = 0
   for num in args:
      total += num
   return total

nums = [1, 2, 3, 4, 5, 6]
sum_all_values(*nums) # * works as an unpacking operator with lists and tuples

# unpacking dictionaries with ** operator
def display_users(user1, user2):
   return f"{user1} and {user2} are users."

users = {"user1": "Alice", "user2": "Bob"}
display_users(**users) # ** works as an unpacking operator with dictionaries

# another example of unpacking dictionaries with ** operator
def add_and_multiply_numbers(a, b, c):
   return a + b * c

data = dict(a=1000, b=2000, c=3000)
add_and_multiply_numbers(**data) # ** works as an unpacking operator with dictionaries
add_and_multiply_numbers(**data, d=4000) # you can add more argyments