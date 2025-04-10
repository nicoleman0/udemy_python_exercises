# def my_decorator(fn):
#     def wrapper(*args, **kwargs):
#         pass
#     return wrapper

# example

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}."


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


print(greet("nick"))
print(order("burger", "fries"))
