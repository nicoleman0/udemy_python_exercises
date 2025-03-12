# function that removes all negative numbers from a list of numbers
# lambda returns True if the number is greater than or equal to 0
# filter returns a new list with only the numbers that return True

def remove_negatives(nums):
    return list(filter(lambda x: x >= 0, nums))

if __name__ == "__main__":
    print(remove_negatives([-1, 3, 4, -99])) #