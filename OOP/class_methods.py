class User:

    active_users = 0    # class attribute

    @classmethod
    # User passed in automatically, because it is the class
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out."

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
        print(f"Happy {self.age}th birthday, {self.first}.")


user1 = User("Nick", "Coleman", 24)
user2 = User("Bob", "Builder", 50)
user3 = User("Maria", "Lopez", 39)

user4 = User.from_string("Brian, Coleman, 56")

print(user4.birthday())
print(User.active_users)
