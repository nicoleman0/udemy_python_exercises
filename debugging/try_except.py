# try/except works like an if/else statement

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None
    
d = {"name": "Ricky"}
get(d, "name") # Ricky
get(d, "city") # None

# try/except/else/finally
# this is a very common structure for input validation

while True:
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print("Nice, you entered a number.")
        break
    finally:
        print("Runs no matter what!")
