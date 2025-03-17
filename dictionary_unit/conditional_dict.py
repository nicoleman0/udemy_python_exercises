# conditional logic with dictionaries
my_list = [10, 15, 28, 33, 51, 68, 89, 92, 103]
even_or_odd = {num: ("even" if num % 2 == 0 else "odd")
               for num in my_list}  # creates new dict
print(even_or_odd)

# range method
odd_or_even = {num: "even" if num %
               2 == 0 else "odd" for num in range(1, 101, 3)}
print(odd_or_even)

# example with list
person = [
    ["name", "Jared"],
    ["job", "Musician"],
    ["city", "Bern"]
]

answer = {i[0]: i[1] for i in person}
answer = dict(person)  # easy version

# vowel: 0
{vowel: 0 for vowel in "aeiou"}
# Output: {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# ASCII conversion dict
{num: chr(num) for num in range(65, 91)}
# Output: {65: 'A', 66: 'B', 67: 'C', 68: 'D', etc.
