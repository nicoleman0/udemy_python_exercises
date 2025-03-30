# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
# NO CONTROL OVER CURSOR
# Always adds to the end of file
with open("haiku.txt", "a") as file:
    file.seek(0)
    file.write(":)\n")

# r+ read and write (allows you to make changes to file anywhere)
# r+ by default adds to beginning of file
with open("haiku.txt", "r+") as file:
    file.write(":)")
    file.seek(10)  # here cursor works
    file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "a") as file:
    file.write("HELLO!!!")
