def add_positive_numbers(x, y):
    # if not valid_expression: raise AssertionError()
    assert x > 0 and y > 0, "Both numbers MUST be positive."
    return x + y


add_positive_numbers(1, 2)  # 3
# add_positive_numbers(-1, 2)  # AssertionError: Both numbers MUST be positive.


def eat_junk(food):
    assert food in ["burger", "chocolate bar",
                    "hot dog", "fried chicken", "ice cream"], "Food must be junk food!"
    return f"Mmmm... That {food} is so delicious."


burger = eat_junk("burger")
print(burger)
