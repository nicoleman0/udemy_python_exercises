# example showing methods for lists
materials = ["rubber", "cotton", "metal"]
print("ORIGINAL LIST:", materials)

# to add one more object to the end of list
materials.append("coal")
print(f"UPDATED LIST: {materials}")

# to add a list of new objects
materials.extend(["compost", "concrete", "wood", "plastic"])
print(f"UPDATED LIST: {materials}")

# to insert a new object
materials.insert(2, "leather")
print(f"UPDATED LIST: {materials}")

