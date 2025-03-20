class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YO BUSINESS")
        return super().__repr__()   # returns the repr of dict()

    def __missing__(self, key):
        print(f"You want '{key}'? Well... it ain't here!")

    def __setitem__(self, key, value):
        print(f"Why do I have to set '{key}' to '{value}'? Ugh. Fine.")
        return super().__setitem__(key, value)  # this actually  updates the dict

    def __contains__(self, key):
        if key == True:
            print("It's in there.")
        else:
            print("It ain't in there.")


data = GrumpyDict({"first": "Nick", "animal": "cat"})
print(data)
data["city"]
data["city"] = "New York City"
print(data)

'food' in data
