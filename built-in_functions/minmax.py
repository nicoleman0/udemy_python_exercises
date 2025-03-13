# max - return the largest item in an iterable, or the largest of two or more arguments
# min - return the smallest item in an iterable, or the smallest of two or more arguments
nums = [1, 2, 3, 4, 5]
max(nums) # 5
min(nums) # 1

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Zoe']

max(names, key=lambda n: len(n)) # 'Samson'

# Find the song with the most plays

songs = [{'title': 'Happy Birthday', 'playcount': 1},
         {'title': 'Survive', 'playcount': 6},
         {'title': 'YMCA', 'playcount': 99},
         {'title': 'Toxic', 'playcount': 31}]

min(songs, key=lambda s: s['playcount']) # {'title': 'Happy Birthday', 'playcount': 1}

max(songs, key=lambda s: s['playcount'])['title'] # 'YMCA'