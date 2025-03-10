# 1

def return_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
    "Thursday", "Friday", "Saturday"]
    if num > 0 and num <= len(days):
        return days[num-1] 
    return None

def user_day_input():
    day = int(input("Enter a number between 1 and 7: "))
    return print(return_day(day))

user_day_input()

# 2

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list):
    if list: 
        return list[-1]
    return None

print(last_element([1,2,3])) # 3