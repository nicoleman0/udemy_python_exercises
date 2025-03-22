def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()    # where the decorator function will be called
        print("Have a great day!")
    return wrapper


@be_polite  # @ makes it a decorator
def greet():
    print("My name is Nick.")


@be_polite
def rage():
    print("I HATE YOU!!!")


rage()
greet()
