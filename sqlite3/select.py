import sqlite3

conn = sqlite3.connect('friends.db')
cursor = conn.cursor()

cursor.execute('''SELECT * FROM friends WHERE closeness > 5
                    ORDER BY closeness DESC''')

# Using a for loop to iterate over the results

for result in cursor:
    print(result)

# using fetchall() to get all results at once
# returns a list of tuples

results = cursor.fetchall()
print(results)

# commit the changes
conn.commit()
conn.close()
