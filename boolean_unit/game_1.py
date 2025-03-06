# just a silly game
print("1. Techmonk\n2. Nunchucker\n3. Expert Griller")

print("Pick your role, and seal your fate...")
print(" ")
role = input()

if role == "Techmonk":
	print("Good choice. You are a techmonk from the lands of everyonder somewhere.")
elif role == "Nunchucker":
	print("A nunchucker? Wow. Been a long time since we've seen your lot.")
else:
	print("An expert GRILLER?! You have quite a legacy to live up to.")

print("Now please tell me where you would like to go.\nDo you want to visit the desert?\nOr the town?\nOr the caves?")
place = input()

if place == "desert" and role == "Techmonk":
	print("You, the Techmonk, travel to the land of Al-Jazir. You see a dragon.")
elif place == "desert" and role == "Nunchucker":
	print("You the Nunchucker, have landed in the lands of Al-Jazir.")
elif place == "desert" and role == "Expert Griller":
	print("You, the EXPERT GRILLER HAVE ENTERED INTO THE LANDS OF AL-JAZIR!!!! YOU SMELL MEAT.")

