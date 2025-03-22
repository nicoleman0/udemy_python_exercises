# multiples function


def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


m = get_multiples(3, 10)
multiples = list(m)
print(multiples)

# unlimited multiples


def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num
