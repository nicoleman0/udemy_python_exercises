class User:

    active_users = 0

    @classmethod
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


class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} total mods online."

    def remove_post(self):
        return f"{self.full_name} removed a post from the {self.community} community."


mod1 = Moderator("Nick", "Coleman", 24, "Python")
u1 = User("James", "Garcia", 39)
u2 = User("Maria", "Stone", 31)
u3 = User("Johnny", "Rockets", 56)
mod2 = Moderator("Tony", "Choppa", 20, "One Piece")

print(User.display_active_users())
print(Moderator.display_active_mods())

print(mod2.full_name())
print(mod1.full_name())
