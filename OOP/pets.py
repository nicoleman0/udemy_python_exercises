class Pet:
    allowed = ["cat", "dog", "fish", "rat", "bird", "hamster"]

    def __init__(self, name, species):
        if self.species not in Pet.allowed:
            raise ValueError(f"You can't have a {self.species} pet!")
        self.name = name
        self.species = species


cat = Pet("Franky", "cat")
dog = Pet("Fido", "dog")
