print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Make your choice, Player 1: ")
print("*** NO CHEATING PLEASE!!!***\n\n" * 20)
player2 = input("Now, make your choice Player 2: ")

if player1 == player2:
	print("Tie game!")
elif player1 == "rock":
	if player2 == "scissors":
		print("player1 wins!")
	elif player2 == "paper":
		print("player2 wins!")
elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins!")
	elif player2 == "scissors":
		print("player2 wins!")
elif player1 == "scissors":
	if player2 == "paper":
		print("player1 wins!")
	elif player2 == "rock":
		print("player2 wins!")
else:
	print("Something went wrong. Maybe because you did not pick a choice.")


## another clearer solution

# p1 = input("Player 1: rock, paper, or scissors ")
# p2 = input("Player 2: rock, paper, or scissors ")
 
# if p1 == p2:
#     print("Draw")
# elif p1 == "rock" and p2 == "scissors":
#     print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
#     print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1 wins")
# else:
#     print("p2 wins")