playlist = {
    'title': 'patagonia bus',
    'author': 'nick coleman',
    'songs': [{'title': 'Turn it Off', 'artist': ['blue'], 'Duration': 2.25},
              {'title': 'Let it Go', 'artist': ['Cindarella'], 'Duration': 3.0},
              {'title': 'song', 'artist': ['blue', 'Mr. Bean'], 'Duration': 4.0},
              {'title': 'BLEH', 'artist': ['Johnny'], 'Duration': 3.2}]

}

# total duration
total_length = 0

for song in playlist['songs']:
    total_length += song['Duration']

print(f"The total length of the playlist is {total_length} mins.")