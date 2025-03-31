from csv import reader, writer

# example 1 - find_user


def find_user(first, last):
    with open('users.csv') as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first == row[0]
            last_name_match = last == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first} {last} not found."

# example 2 - update_users


def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)

    return f"Users updated: {count}."

# example 3 - delete_users


def delete_users(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            # this skips over writing if they match
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                # this writes if they match, opposite of removal
                csv_writer.writerow(row)
    return f"Users deleted: {count}."
