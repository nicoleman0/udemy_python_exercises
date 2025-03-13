# zip - combine two or more iterables into a single iterable
# zip stops when the shortest input iterable is exhausted (zip is lazy)
first_zip = zip([1, 2, 3], [4, 5, 6])
list(first_zip) # [(1, 4), (2, 5), (3, 6)]
dict(first_zip) # {1: 4, 2: 5, 3: 6}

# example - combine two lists into a list of tuples
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

z = zip(nums1, nums2) # <zip object at 0x7f9b1c5f3d40>
list(z) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# example of zip stopping when the shortest input iterable is exhausted
nums1 = [1, 2, 3]
nums2 = [4, 5, 6, 7, 8]

z = zip(nums1, nums2)
list(z) # [(1, 4), (2, 5), (3, 6)]

# example - combine three lists into a list of tuples
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
words = ['one', 'two', 'three']
z2 = zip(nums1, nums2, words)
list(z2) # [(1, 4, 'one'), (2, 5, 'two'), (3, 6, 'three')]

# example - combine two lists into a list of tuples and then unzip the result
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

five_by_two_unzipped = list(zip(*five_by_two))

five_by_two_unzipped # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]