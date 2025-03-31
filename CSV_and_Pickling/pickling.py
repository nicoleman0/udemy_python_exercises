import pickle


class Pet:

    allowed = ["cat", "dog", "fish", "rat", "bird", "hamster"]

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {self.species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.species:
            raise ValueError(f"You can't have a {self.species} pet!")
        self.species = species


cat = Pet("Franky", "cat")

# Pickling
with open("pets.pickle", "wb") as file:  # wb makes data binary
    pickle.dump(cat, file)

# Getting it back out
with open("pets.pickle", "rb") as file:
    zombie_cat = pickle.load(file)
    print(zombie_cat.name)
