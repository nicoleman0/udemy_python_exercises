class User:
    def __init__(self, first, last, age):  # self is a way of referring to specific instances
        self.first = first  # the varibale name doesn't have to match the parameter name
        self.last = last
        self.age = age


user1 = User("Nick", "Coleman", 24)
user2 = User("Bob", "Builder", 50)

print(user1.first)   # to access specific attributes you run instance.attribute_name
print(user2.first, user2.last, user2.age)


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


toyota = Vehicle("Toyota", "Camry", 2024)
print(toyota.make, toyota.model, toyota.year)
