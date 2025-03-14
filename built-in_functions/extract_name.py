def extract_full_name(l):
    return list(
        map(lambda val: f"{val['first']} {val['last']}", l)
        )

# Test usage

people = [
    {'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'Tim', 'last': 'Garcia'},
    {'first': 'Matt', 'last': 'Lane'},
    {'first': 'Colt', 'last': 'Steele'}
]

full_names = extract_full_name(people)

if __name__ == '__main__':
    print(full_names)  # Output: ['Elie Schoppik', 'Tim Garcia', 'Matt Lane', 'Colt Steele']
