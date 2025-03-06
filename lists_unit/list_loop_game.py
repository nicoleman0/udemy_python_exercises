# a simple code experiment using lists 'n loops
from random import randint

player_class = input("Please choose your class...\nKnight\nMonk\nWizard\n").lower()
if player_class == "knight":
    player_health = 100 + randint(1,20)
    player_magic = 10 + randint(1,3)
    player_attack = 20 + randint(1,5)
elif player_class == "monk":
    player_health = 14 + randint(1,4)
    player_magic = 10 + randint(1,5)
    player_attack = 20 + randint(1,12)
else:
    player_health = 80 + randint(1,5)
    player_magic = 20 + randint(1,10)
    player_attack = 10 + randint(1,3)

weapons = ["sword", "staff", "knife", "nunchucks", "axe", "mace"]

print("Now choose your weapon!")
for weapon in weapons:
    print(weapon)

weapon = input("Which weapon do you choose?\n")

if weapon == weapons[0]:
    weapon_damage = 4
elif weapon == weapons[1]:
    weapon_damage = 2
elif weapon == weapons[2]:
    weapon_damage = 1
elif weapon == weapons[3]:
    weapon_damage = 3
elif weapon == weapons[4]:
    weapon_damage = 5
elif weapon == weapons[5]:
    weapon_damage = 5
else:
    print("You picked nothing.")
