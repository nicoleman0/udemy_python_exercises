from csv import reader


def find_user(first, last):
    with open('users.csv') as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first == row[0]
            last_name_match = last == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first} {last} not found."
