# practice with *args
def sum_of_nums(*nums):  # can be anything, but *args is a common convention
    """Takes in any number of arguments and returns their sum.
    >>> sum_of_nums(1, 2, 3)
    6

    >>> sum_of_nums(100, 200, 300)
    600

    >>> sum_of_nums('a', 100)
    Traceback (most recent call last):
      File "/usr/lib/python3.12/doctest.py", line 1361, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest sum_of_nums.sum_of_nums[2]>", line 1, in <module>
        sum_of_nums('a', 100)
      File "/home/nicholas-coleman/Desktop/udemy_python/functions_unit/Part-2/sum_of_nums.py", line 19, in sum_of_nums
        total += num
    TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    """
    total = 0
    for num in nums:
        total += num
    return total


def ensure_correct_info(*args):
    if "Nick" in args and "Coleman" in args:
        return "Welcome back Nick!"

    return "Not sure who you are..."


# can pass in any number of arguments, but must include Nick and Coleman
print(ensure_correct_info(1, True, "Nick", "Coleman"))
