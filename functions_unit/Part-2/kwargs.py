# **kwargs - keyword arguments
def fav_sports(**kwargs):
    for person, sport in kwargs.items():
        print(f"{person}'s favorite sport is {sport}")

fav_sports(Nick="Hockey", John="Football", Angela="Basketball")