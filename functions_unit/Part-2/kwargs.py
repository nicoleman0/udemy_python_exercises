# **kwargs - keyword arguments
def fav_sports(**kwargs):
    for person, sport in kwargs.items():
        print(f"{person}'s favorite sport is {sport}")

fav_sports(Nick="Hockey", John="Football", Angela="Basketball")

def secret_greeting(**kwargs):
    if "Nick" in kwargs and kwargs["Nick"] == "open sesame":
        print("You may enter!")
    elif "Nick" in kwargs:
        print(f"Wrong password.")
    return "You're not Nick."

if __name__ == "__main__":
    secret_greeting(Nick="open sesame")
