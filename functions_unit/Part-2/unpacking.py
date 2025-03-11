# using * as an argument
def sum_all_values(*args):
   total = 0
   for num in args:
      total += num
   return total

nums = [1, 2, 3, 4, 5, 6]
sum_all_values(*nums) # * works as an unpacking operator with lists and tuples