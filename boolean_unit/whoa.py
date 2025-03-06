print("Do you like to eat chocolate?: ")
choco = input()

if choco == "Yes":
	return True
else:
	print("That's ok. Do you have another favorite snack?: ")
	snack = input()

if choco == True:
	print("Brooooo. Nice.")
else:
	print(f"Ok {snack} is a good choice.")