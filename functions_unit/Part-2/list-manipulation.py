'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(lst, command, location, value=None):
    if command == "remove" and location == "end":
        return lst.pop()
    elif command == "remove" and location == "beginning":
        return lst.pop(0)
    elif command == "add" and location == "beginning":
        lst.insert(0, value)
        return lst
    else:
        lst.append(value)
        return lst 