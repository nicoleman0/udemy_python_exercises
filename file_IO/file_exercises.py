# copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same


def copy(filename, new_filename):
    with open(filename) as file:
        text = file.read()  # reading it to a variable

    with open(new_filename, "w") as new_file:
        new_file.write(text)


# copy_and_reverse('story.txt', 'story_reversed.txt')  # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt


def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

# statistics('story.txt')
# {'lines': 172, 'words': 2145, 'characters': 11227}


def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        return {
            "lines": len(lines),
            "words": sum(len(line.split(" ")) for line in lines),
            "characters": sum(len(line) for line in lines)
        }


# find_and_replace('story.txt', 'Alice', 'Colt')
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland


def find_and_replace(file_name, word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
