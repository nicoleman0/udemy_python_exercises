# practice with *args
def sum_of_nums(*args): # can be anything, but *args is a common convention
   total = 0
   for num in args:
      total += num
   return total

def ensure_correct_info(*args):
   if "Nick" in args and "Coleman" in args:
        return "Welcome back Nick!"
   
   return "Not sure who you are..."

print(ensure_correct_info(1, True, "Nick", "Coleman")) # can pass in any number of arguments, but must include Nick and Coleman