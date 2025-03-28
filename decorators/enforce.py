def enforce(*types):
    def decorator(fn):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (arg, type) in zip(args, types):
                newargs.append(type(arg))    # type check/conversion
            return fn(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)  # *types passed in
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a/b)


@enforce(str, str)
def hello(first, last):
    print(f"Hello {first} {last}")


repeat_msg("hello", '3')
divide('1', '4')

hello("Nick", "Coleman")
