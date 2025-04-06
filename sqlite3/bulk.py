import sqlite3

conn = sqlite3.connect('friends.db')

cursor = conn.cursor()

people = [
    ("Nick", "Jones", 7),
    ("Jim", "Smith", 5),
    ("Barack", "Obama", 10),
    ("George", "Bush", 3),
    ("Bill", "Clinton", 8),
    ("Donald", "Trump", 2),
    ("Joe", "Biden", 9),
    ("Hillary", "Clinton", 6),
    ("Bernie", "Sanders", 4),
    ("Kamala", "Harris", 1)
]

# option 1
cursor.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

# option 2
for person in people:
    cursor.execute("INSERT INTO friends VALUES (?, ?, ?)", person)

conn.commit()
conn.close()
