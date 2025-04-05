import re

# r - raw string, good to use
regex_phone = re.compile(r'\d{3} \d{3}-\d{4}')
regex_url = re.compile(r'https?://(www\.)?([A-Za-z_-]+\.[A-Za-z]{3})')


res = regex_phone.search("Call me at 915 349-1234")
print(res.group())

res = regex_phone.findall("Call me at 915 349-1234 or 915 302-3059")
print(res)

# another method
res = re.search(r'\d{3} \d{3}-\d{4}', "Call me at 808 847-0929").group()
print(res)

# example -> for finding binary bytes
bytes_regex = re.compile(r'\b[01]{8}\b')


def parse_bytes(bytes):
    match = bytes_regex.findall(bytes)
    if match:
        return list(match)
    return None
