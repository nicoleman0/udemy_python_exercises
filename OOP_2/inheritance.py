# Example with property


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


nick = Human("Nick", "Jones", 30)
print(nick.age)  # this works because of the age property
nick.age = 45
print(nick.age)
print(nick.full_name)
nick.full_name = "Corey Schafer"
print(nick.__dict__)
