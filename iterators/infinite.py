# infinite loop


def current_beat():
    nums = [1, 2, 3, 4]
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1

# beat generator


def make_song(num=99, beverage="soda"):
    for num in range(num, -1, -1):  # stops at 0
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield f"Only {num} bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"


snapple_song = make_song(5, "snapple")
print(next(snapple_song))
print(next(snapple_song))
print(next(snapple_song))
print(next(snapple_song))
print(next(snapple_song))
print(next(snapple_song))
