colors = ["purple", "teal", "magenta", "crimson", "emerald"]
index = 0 


# the for loop (much better for this situation)
for color in colors:
    print(color)

# the while loop
while index < len(colors):
    print(f"{index + 1}: {colors[index]}")
    index += 1
