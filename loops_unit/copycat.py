# repeat everything until user says "stop copying me"

ans = input("Hey there! How ya doin' today?\n")
secret = "please stop copying me"


while ans != secret:
	print(ans)
	ans = input()

if ans == secret:
	print("UGH FINE YOU WIN")