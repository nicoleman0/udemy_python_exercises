def max_magnitude(nums):
    return max(abs(num) for num in nums)

print(max_magnitude([300, 20, -900]))  # 900

# define sum_even_values
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

# define sum_floats
def sum_floats(*args):
    return sum(num for num in args if type(num) == float)