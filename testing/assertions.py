def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers MUST be positive."
    return x + y


add_positive_numbers(1, 2)  # 3
add_positive_numbers(-1, 2)  # AssertionError: Both numbers MUST be positive.
