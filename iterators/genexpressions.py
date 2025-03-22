# generator expressions
example = (num for num in range(1, 20))   # generator object

print(next(example))
print(next(example))
print(next(example))

total = sum(num for num in range(1, 50))
print(total)

l = [num for num in range(1, 20)]   # list comprehension
print(l)
