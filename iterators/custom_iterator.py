class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

# Using a generator instead


def count_up_to(high):
    count = 0
    while count < high:
        yield count  # yield retains previous state unlike basic functions
        count += 1


# week exercise

def week():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day

# yes or no exercise


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"
