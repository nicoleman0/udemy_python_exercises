# Common commands for pdb
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
# q (quit)

first = "First"
second = "Second"

import pdb; pdb.set_trace() # This is a breakpoint, put it where you want to stop the code

result = first + second
third = "Third"
result += third
print(result)