import sqlite3

conn = sqlite3.connect('friends.db')
# create cursor object
cursor = conn.cursor()
# execute some SQL

# cursor.execute(
#     '''CREATE TABLE IF NOT EXISTS friends
#         (name TEXT, last_name TEXT, closeness INTEGER)''')
# insert_query = '''INSERT INTO friends
#         VALUES ("Nick", "Jones", 7)'''
# cursor.execute(insert_query)

# example of sanitizing user input using parameterized queries

# first_form = "Jim"
# query = "INSERT INTO friends (name) VALUES (?)"
# conn.execute(query, (first_form,))

data = ("Barack", "Obama", 10)
query = '''INSERT INTO friends (name, last_name, closeness)
                VALUES (?,?,?)'''
conn.execute(query, data)

# commit the changes
conn.commit()
conn.close()
