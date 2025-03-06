# calypso's color game

print("Hello there. What is your name, lone traveler of the misty mists?")
name = input()

if name == "Calypso":
	print("Calypso! How long it's been since we've last seen you. We are forever in your debt.")
else:
	print(f"Ok. Nice to meet you {name}.")

print(f"Tell me, {name}... What is your favorite color?")
color = input()

if color == 'purple':
	print("Oh you definitely are the chosen one. All hail " + name + "!!!")
elif color == 'yellow':
	print("That's disgusting.")
elif color == 'blue':
	print("Blue is a good color. Gotta admit.")
elif color == 'black':
	print("Yeah. Black is one of the best.")
elif color == 'green':
	print("Hmm. Good choice I guess.")
else:
	print("Mediocre.")