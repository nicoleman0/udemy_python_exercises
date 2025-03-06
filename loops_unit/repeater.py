times = int(input("How many times do I have to tell you to clean?\n"))

for time in range(times): # for x in range(0, y)
	print("CLEAN YOUR ROOM!")
	if time >= 3:
		print("I give up.")
		break 