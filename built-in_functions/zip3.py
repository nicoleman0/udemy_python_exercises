# Description: Interleave two strings

def interleave(str1, str2):
    return ''.join(''.join(i) for i in zip(str1, str2))

if __name__ == '__main__':
    print(interleave('hi', 'ha')) # Output: 'hhia'

# Triple and filter

# return list of numbers divisible by 4, multipled by 3

def triple_and_filter(numlist):
   """return list of numbers divisible by 4, multipled by 3"""
   return list(
       filter(
           lambda x: x % 4 == 0, map(lambda x: x * 3, numlist)
           )
       )
