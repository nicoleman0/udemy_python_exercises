# Method Resolution Order
# the order in which Python resolves methods on a class, influenced by inheritance

class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    def do_something(self):
        print("Method Defined In: B")


class C(A):
    def do_something(self):
        print("Method Defined In: C")


class D(B, C):
    def do_something(self):
        print("Method Defined In: D")


print(D.__mro__)
print(D.mro())
# print(help(D)) -> the best one

thing = D()
thing.do_something()
