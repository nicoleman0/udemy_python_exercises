import random

prize = random.randint(1, 100)

if prize >= 51:
	print(f"You have won! Your score was: {prize}!")
else:
	print(f"Too bad. A score of {prize} is not good enough...")