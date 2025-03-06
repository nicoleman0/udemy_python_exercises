import random

random_number = random.randint(1,10) #1-10

while True:
	guess = int(input("Pick a number from 1 to 10: "))
	if guess < random_number:
		print("TOO LOW! TOO SLOW!")
	elif guess > random_number:
		print("TOO HIGH!")
	else: 
		print("YOU WON!!!")
		play_again = input("Do you wan to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break
