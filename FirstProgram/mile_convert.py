print("How many kilometers do you wish to convert?")
kms = input()

miles = float(kms)/1.60934 # must convert the kms input into float to divide
miles = round(miles, 2)

print(f"{kms} kilometers is equal to {miles} miles.")