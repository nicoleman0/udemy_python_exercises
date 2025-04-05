import re

regex_phone = re.compile(r'\b\d{3} \d{3}-\d{4}\b')


def extract_phone(input):
    match = regex_phone.search(input)
    if match:
        return match.group()
    return None


def extract_all_phones(input):
    match = regex_phone.findall(input)
    if match:
        return match
    return None


def verify_phone(input):
    match = regex_phone.fullmatch(input)
    if match:
        return True
    return False


extracted = extract_phone("Call me at 915 349-1234")
print(extracted)

extraced_numbers = extract_all_phones(
    "Call me at 915 349-1234 or 915 302-3059")
print(extraced_numbers)

print(verify_phone("915 349-1234"))
