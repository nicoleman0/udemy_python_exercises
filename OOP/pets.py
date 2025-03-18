class Pet:

    allowed = ["cat", "dog", "fish", "rat", "bird", "hamster"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {self.species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):  # to prevent changing species
        if species not in Pet.species:
            raise ValueError(f"You can't have a {self.species} pet!")
        self.species = species


cat = Pet("Franky", "cat")
dog = Pet("Lorenzo", "dog")

print(f"{dog.name} the {dog.species}")
