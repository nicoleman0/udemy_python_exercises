# Scope: The scope of a variable is the region of your program in which it is defined.

# Global Scope: A variable created in the main body of the Python code is a 
# global variable and belongs to the global scope.

# Local Scope: A variable created inside a function belongs to the local scope of that function
# and can only be used inside that function.

total = 0
def increment():
    global total # use the global keyword to declare that the variable is global
    total += 1
    return total 

print(increment())