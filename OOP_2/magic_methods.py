class Human:
    def __init__(self, name="a human"):
        self.name = name

    def __repr__(self):
        return self.name


dude = Human()
print(dude)
