class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"


class Cat(Animal):  # Cat class inherits from Animal class
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # super refers to the base/super class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


franky = Cat("Franky", "Russian Blue", "String")
print(franky)
franky.play()
