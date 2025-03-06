# make a guessing game where guess the number betweeen 1-10
# the computer chooses a number for you to guess

from random import randint

cpu_choice = randint(1,11)

guess = int(input("Make your guess!\n"))

while guess != cpu_choice:
	yes_or_no = (input("Sorry, you guess wrong.\nDo you want to try again? (y/n): "))
	if yes_or_no == "y":
		cpu_choice = randint(1,11)
		guess = int(input("Make your guess again:\n"))
	else:
		break
print("You guessed right! Congrats.")