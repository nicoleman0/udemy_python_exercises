from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}."

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        raise TypeError("You can't add that!")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError("You can't multiply that!")


n = Human("Nick", "Coleman", 24)
l = Human("Laura", "van Djik", 24)

# Experiment with multiplied copies
triplets = n * 3
print(triplets)
triplets[0].first = "James"
print(triplets)

# nick and laura having triplets
triplets = (n + l) * 3
print(triplets)
