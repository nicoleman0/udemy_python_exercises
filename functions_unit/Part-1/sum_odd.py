def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total # remember to fix the indent, or it will end

print(sum_odd_numbers(range(1, 101)))


# WRONG VERSION 
# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#         return total

# print(sum_odd_numbers(range(1, 101)))