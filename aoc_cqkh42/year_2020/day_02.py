import re

REGEX = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


def part_a(data):
    lines = (re.match(REGEX, line).groups() for line in data.split('\n'))
    is_valid = (
        int(low) <= pw.count(char) <= int(high)
        for low, high, char, pw in lines
    )
    return sum(is_valid)


def part_b(data, **_):
    lines = (re.match(REGEX, line).groups() for line in data.split('\n'))
    extracted = (
        (pw[int(low)-1] + pw[int(high)-1], char)
        for low, high, char, pw in lines
    )
    is_valid = (tokens.count(char) == 1 for tokens, char in extracted)
    return sum(is_valid)
