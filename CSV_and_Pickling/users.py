from csv import DictWriter

with open("CSV_and_Pickling/users.csv", "w") as file:
    headers = ["Username", "Age", "Role", "System ID"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Username": "nicoleman",
        "Age": 24,
        "Role": "Security Analyst",
        "System ID": 12002
    })
    csv_writer.writerow({
        "Username": "jhorn",
        "Age": 30,
        "Role": "Security Engineer",
        "System ID": 14239
    })
    csv_writer.writerow({
        "Username": "lijenning",
        "Age": 28,
        "Role": "Incident Responder",
        "System ID": 15438
    })
