from functools import wraps


def double_return(fn):
    @wraps(fn)
    def wrappper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [result, result]
    return wrappper
