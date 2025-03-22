# when assigning a decorator, it's information is replaced
# to stop this, you have to include @wraps

from functools import wraps


def log_function_data(fn):
    @wraps(fn)  # preserves the name & docstring of decorator func
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together."""
    return x + y


print(add.__doc__)
print(add.__name__)
# help(add)
