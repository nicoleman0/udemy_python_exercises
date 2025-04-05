import re

name_regex = re.compile(
    r'(?P<prefix>^Mr\.|Mrs\.|Ms\.) (?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)')

name = input("What is your name?")

res = name_regex.search(name)

prefix = res.group('prefix')
first_name = res.group('first')
last_name = res.group('last')


print(f"Hello {prefix} {first_name} {last_name}. Nice to meet you.")
