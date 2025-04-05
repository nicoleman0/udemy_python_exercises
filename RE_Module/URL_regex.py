import re

url_regex = re.compile(
    r'(https?)://(www\.[A-Za-z-]{2,256})(\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')


def valid_url(input):
    match = url_regex.fullmatch(input)
    if match:
        return match.groups()
    return False


url = "https://www.webmd.com/mental-health/default.htm"

protocol = valid_url(url)[0]
domain_name = valid_url(url)[1]
top_level_domain = valid_url(url)[2]
path = valid_url(url)[3]


def url_parts():
    print(f"Protocol: {protocol}")
    print(f"Domain Name: {domain_name}")
    print(f"Top Level Domain: {top_level_domain}")
    print(f"Page Path: {path}")


url_parts()
