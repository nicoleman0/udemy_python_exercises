from time import time
from functools import wraps


def speedtest(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time() - start_time
        print(f"{func.__name__} ran in {end_time} seconds.")
        print(f"Result: {result}")
        return result
    return wrapper


@speedtest
def sum(num):
    """Sum of all numbers from 1 to num"""
    total = 0
    for i in range(num):
        total += i
    return total


help(speedtest)
