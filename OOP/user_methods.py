class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):    # instance method
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def hobby(self, hobby):
        return f"{self.first}'s favorite hobby is {hobby}."

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday! Happy {self.age}th birthday, {self.first}.")


user1 = User("Nick", "Coleman", 24)
username = user1.full_name()
print(username)

inits = user1.initials()
print(inits)

fav_hobby1 = user1.hobby("hiking")
print(fav_hobby1)

seniority = user1.is_senior()
print(seniority)

print(user1.birthday())
