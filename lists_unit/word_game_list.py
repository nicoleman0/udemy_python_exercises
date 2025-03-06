# iterate over the list, and add all the words together
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# word is empty so the sounds can be added
word = ""

# loop iterates over list, adds each s from sounds to word
for s in sounds:
    word += s.upper()

print(word)