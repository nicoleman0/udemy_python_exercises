from functools import wraps

# double return exercise


def double_return(fn):
    @wraps(fn)
    def wrappper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result, result]
    return wrappper

# fewer than three args


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            return "Too many arguments!"
        return fn(*args, **kwargs)
    return wrapper

# only ints


def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return fn(*args, **kwargs)
    return inner

# authorization


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper
