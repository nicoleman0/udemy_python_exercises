print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Make your choice, Player 1: ")
player2 = input("Now, make your choice Player 2: ")

if player1 == "rock" and player2 == "scissors":
	print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
	print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
	print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
	print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
	print("Player 1 wins!")
elif player1 == "scissors" and player2 == "rock":
	print("Player 2 wins!")
elif player1 == player2:
	print("It is a tie game.")
else:
	print("You probably did not pick rock, paper, or scissors.")