import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

# This regex will match the prefix (Mr., Mrs., Ms.) and the first letter of the name
# and replace the rest of the name with nothing.
pattern = re.compile(
    r'(?P<prefix>Mr.|Mrs.|Ms.) (?P<first_letter>[a-z])[a-z]+', re.I)

result = pattern.sub("\g<prefix> \g<first_letter>", text)

print(result)

# CENSORED


def censor(sentence: str):
    # \b to prevent false positives if "fuck" occurs in the middle of another word
    pattern = re.compile(r'(\bfuck\w*\b)', re.I)
    if pattern:
        return pattern.sub("CENSORED", sentence)
    else:
        return sentence


censored_text = censor("Fuck you fucker.")

print(censored_text)
