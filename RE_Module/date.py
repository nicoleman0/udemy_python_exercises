import re


def parse_date(date: str) -> dict:
    date_regex = re.compile(
        r'^(?P<day>\b\d{2})[/.,](?P<month>\d{2})[/.,](?P<year>\d{4}\b)$')
    match = date_regex.search(date)
    if match:
        return {
            'd': match.group('day'),
            'm': match.group('month'),
            'y': match.group('year')
        }
    else:
        raise ValueError(
            "Invalid date format. Expected dd/mm/yyyy or dd-mm-yyyy.")
