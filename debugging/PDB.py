import pdb
first = "First"
second = "Second"

pdb.set_trace() # This is a breakpoint, put it where you want to stop the code

result = first + second
third = "Third"
result += third
print(result)