# reversed - returns a reversed iterator (not a list) of the input sequence
# reversed(seq)
# for lists you use reverse(list) method or slicing list[::-1]

# reversed()
for char in reversed("hello world"):
    print(char)

# slicing version (easiest)
"hello"[::-1] # 'olleh'

# really obtuse version
reverse_hello = ''.join(list(reversed("hello"))) # 'olleh'
print(reverse_hello)

# reversed() with range

for x in reversed(range(0, 10)):
    print(x)