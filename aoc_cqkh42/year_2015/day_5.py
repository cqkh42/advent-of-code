import itertools
import re


def _is_nice_a(string):
    vowels = sum(char in 'aeiou' for char in string) >= 3
    repeating_char = max([len(list(group)) for _, group in itertools.groupby(string)]) >= 2
    phrases = not ('ab' in string or 'cd' in string or 'pq' in string or 'xy' in string)
    return vowels and repeating_char and phrases


def _is_nice_b(string):
    repeats = re.search(r'([a-z]{2}).*\1', string)
    one_between = re.search(r'([a-z]).\1', string)
    return bool(repeats and one_between)


def part_a(data):
    return sum(_is_nice_a(string) for string in data.split('\n'))


def part_b(data, **_):
    return sum(_is_nice_b(string) for string in data.split('\n'))
