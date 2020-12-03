import re

REPEATING_CHAR = re.compile(r'(\w)\1')
REPEATING_CHARS = re.compile(r'(\w{2}).*\1')
REPEATING_SPACED = re.compile(r'(\w).\1')


def _is_nice_a(string):
    # noinspection SpellCheckingInspection
    vowels = sum(string.count(vowel) for vowel in 'aeiou') >= 3
    repeating_char = REPEATING_CHAR.search(string)
    bad_phrases = ['ab', 'cd', 'pq', 'xy']
    phrases = all(phrase not in string for phrase in bad_phrases)
    return all((vowels, repeating_char, phrases))


def _is_nice_b(string):
    repeats = REPEATING_CHARS.search(string)
    one_between = REPEATING_SPACED.search(string)
    return bool(repeats and one_between)


def part_a(data):
    return sum(_is_nice_a(string) for string in data.split('\n'))


def part_b(data, **_):
    return sum(_is_nice_b(string) for string in data.split('\n'))
