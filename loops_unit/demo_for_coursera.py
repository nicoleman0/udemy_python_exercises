with open("login_attempts.txt", "r") as file:
	file_text = file.read()
usernames = file_text.split()

# Create function that counts a user's failed login attempts
def login_check(login_list, current_user):
	counter = 0
	for i in login_list:
		if i == current_user:
			counter = counter + 1
	if counter >= 3:
		return "You have tried to login three times. You are locked."
	else:
		return "You can login!"

	login_check(usernames, "elarson")

	# checks if user can login, less than 3 logins 