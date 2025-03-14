def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as err:
        print("Do not DIVIDE by ZERO!")
        print(err)
    except TypeError as err:
        print("Both arguments MUST be ints or floats.")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

divide(10, 'a')