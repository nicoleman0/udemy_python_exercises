class User:

    active_users = 0    # class attribute

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

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
        print(f"Happy Birthday! Happy {self.age}th birthday, {self.first}.")


user1 = User("Nick", "Coleman", 24)
user2 = User("Bob", "Builder", 50)
user3 = User("Maria", "Lopez", 39)

print(User.display_active_users())  # calling class method
