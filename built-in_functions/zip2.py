students = ['Dan', 'Ann', 'Joe', 'Ben', 'Jen']
midterms = (90, 69, 87, 72, 95)
finals = (98, 74, 78, 88, 90)

# zip with list comprehension
final_grades = [max(pair) for pair in zip(midterms, finals)]
print(final_grades)

# zip with dictionary comprehension

# student: max(midterms[0], finals[0] for all items in the zip)

final_grades_dict = {i[0]: max(i[1], i[2]) for i in zip(students, midterms, finals)}

print(final_grades_dict)

# Using map, lambda and zip
# map(function, iterable)

grades = zip(
    students,
    map(
        lambda pair: max(pair), 
        zip(midterms, finals)
        )
)

print(dict(grades)) # Output: {'Dan': 98, 'Ann': 74, 'Joe': 87, 'Ben': 88, 'Jen': 95}