# ordering parameters
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

def display_info(a, b, *args, student="Nick", **kwargs):
    return [a, b, args, student, kwargs]

print(display_info(1, 2, 3, last_name="Coleman", job="Analyst"))

# a - 1
# b - 2
# args - (3,) - sinlge item tuple
# student - "Nick"
# kwargs - {'last_name': 'Coleman', 'job': 'Analyst'}
