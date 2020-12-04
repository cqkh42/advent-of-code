from collections import Counter


def _valid_passphrase_a(phrase):
    words = phrase.split()
    return len(words) == len(set(words))


def _valid_passphrase_b(phrase):
    sorted_strings = [tuple(sorted(word)) for word in phrase.split()]
    return len(sorted_strings) == len(set(sorted_strings))


def part_a(data):
    valid = (_valid_passphrase_a(phrase) for phrase in data.split('\n'))
    return sum(valid)


def part_b(data, **_):
    valid = (_valid_passphrase_b(phrase) for phrase in data.split('\n'))
    return sum(valid)