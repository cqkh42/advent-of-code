import re
import string

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    answer_a = None

    def part_a(self):
        data = _next_password(self.data)
        while not _is_valid(data):
            data = _next_password(data)
        self.answer_a = data
        return data

    def part_b(self):
        a = _next_password(self.answer_a)
        while not _is_valid(a):
            a = _next_password(a)
        return a

REGEX = re.compile(r'([a-z])\1')
THREE_LETTERS = zip(
    string.ascii_lowercase,
    string.ascii_lowercase[1:],
    string.ascii_lowercase[2:]
)
THREE_LETTERS = [''.join(letters) for letters in THREE_LETTERS]


def _next_password(password):
    password = list(reversed(password))
    for index, char in enumerate(password):
        if char == 'z':
            password[index] = 'a'
        else:
            to_add = 1 + (char in 'hnk')
            password[index] = chr(ord(char) + to_add)
            break
    new_password = ''.join(password[-1::-1])
    return new_password


def _is_valid(password):
    has_sequence = any(letters in password for letters in THREE_LETTERS)
    pairs = REGEX.findall(password)
    pairs_count = len(pairs) >= 2
    return has_sequence and pairs_count
