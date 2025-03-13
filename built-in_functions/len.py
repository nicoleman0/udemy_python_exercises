# Description: how len works behind the scenes

len('hi')

'hi'.__len__() # this is how len works behind the scenes

# example of using .__len__() / dunder method
# this is how you can override the len function

class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self): # just look here
        return 50 # returns 50 for length no matter what
    
l1 = SpecialList([1, 2, 3])
print(len(l1)) # 50