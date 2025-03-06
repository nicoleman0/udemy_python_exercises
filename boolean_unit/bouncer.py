# bouncer asking for age

age = input("How old are you?: ")

if age != "":	# if age is not falsy
	age = int(age)
	if age >= 21:
		print("You can drink, so you can just enter normally.")
	elif age >= 18:
		print("You can enter, but you will need a wristband!")
	else:
		print("What are you doing at a nightclub? You are too young!")
else: 
	print("You must enter an age...")