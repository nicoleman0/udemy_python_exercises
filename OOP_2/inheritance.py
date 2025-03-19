class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):  # Cat class inherits from Animal class
    pass


Franky = Cat()
Franky.make_sound("meow")

print(Franky.cool)
print(isinstance(Franky, Cat))
print(isinstance(Franky, object))
