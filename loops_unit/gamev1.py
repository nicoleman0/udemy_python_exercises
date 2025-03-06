# ideas to add to the cpu vs human duel:
    # increasing levels of difficulty, if you can beat the first
    # include a critical hit feature 

from random import randint
max_turns = 12
player_health = 100
player_atk = 12

computer_health = 60
computer_atk = 15

while max_turns > 0 and player_health > 0 and computer_health > 0:
    print("The computer is about to attack you. PLEASE, DO SOMETHING!")
    input("Press ENTER to roll the die and do damage!\n")
    
    # player's turn
    
    player_roll = randint(1,6)
    if player_roll > 3:
        computer_health -= player_atk
        print(f"You just did {player_roll} damage! Nice job!")
    elif player_roll == 6:
        print(f"That was a CRITICAL hit! You just scored {player_roll} damage!!!")
        computer_health -= player_atk * 2
    else:
        print("You did no damage. Sorry.")

    # computer's turn

    print("Now it is the computer's turn to attack you!\n")
    computer_roll = randint(1,6)
    if computer_roll > 2:
        player_health -= computer_atk
        print(f"The computer just did {computer_roll} damage to you!")
    elif computer_roll == 6:
        print(f"Uh oh. The computer scored a CRITICAL hit! It just scored {computer_roll} damage!!!")
        player_health -= computer_atk * 2
    else:
        print("The computer missed and did no damage. Lucky you!")

    # end of turn summary

    print(f"You now have {player_health} health left. The computer has {computer_health} left.\n")
    print(f"There are {max_turns} turns left in this match.")
    
    if computer_health > player_health:
        print("Oof. You died. That really, really, really sucks! Doesn't it? You were so close too. Or maybe not?")
    
    max_turns -= 1
    
if max_turns == 0:
    print("The game is over. There are no turns left. ")
