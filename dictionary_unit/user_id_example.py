users = [
    {
        "user_id": "nicoleman",
        "id_number": "948201",
        "device_id": "A923N09",
        "job": "security analyst"
    },
    {
        "user_id": "lodeman",
        "id_number": "493210",
        "device_id": "A924N09",
        "job": "security engineer"
    }
]

# Accessing user data
print(users[0]["user_id"])  # Output: nicoleman
print(users[1]["job"])     # Output: security engineer

# Iterating through users
for user in users:
    print(f"User ID: {user['user_id']}, Job: {user['job']}")