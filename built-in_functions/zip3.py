# Description: Interleave two strings
def interleave(str1, str2):
    return ''.join(''.join(i) for i in zip(str1, str2))

if __name__ == '__main__':
    print(interleave('hi', 'ha')) # Output: 'hhia'
