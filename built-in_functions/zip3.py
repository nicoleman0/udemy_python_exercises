# Description: Interleave two strings

def interleave(str1, str2):
    return ''.join(''.join(i) for i in zip(str1, str2))

if __name__ == '__main__':
    print(interleave('hi', 'ha')) # Output: 'hhia'

# Triple and filter

def triple_and_filter(numlist):
   return list(
       filter(
           lambda x: x % 4 == 0, map(lambda x: x * 3, numlist)
           )
       )
