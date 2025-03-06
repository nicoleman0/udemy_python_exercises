# print a beautiful piece of art involving smiley emojis
# smiley face = "\U0001f600"
# 1 - 10 smileys

emoji = "\U0001f600"

# normal for loop
for num in range(1,11):
	print(emoji * num)

# nested for loop
for x in range(3):
	for num in range(1,11):
		print(emoji * num)

# while
times = 1 
while times <= 10:
	print(emoji * times)
	times += 1

# while/for loop
for num in range(1,11):
	count = 1
	smileys = ""
	while count < num:
		smileys += "\U0001f600"
		count += 1
print(smileys)