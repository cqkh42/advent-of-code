import itertools
import re
import string

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    answer_a = None

    def parse_data(self):
        return [string.ascii_lowercase.index(char) for char in self.data]

    def part_a(self):
        data = _next_password(self.parsed_data)
        while not _is_valid(data):
            data = _next_password(data)
        self.answer_a = data
        a = [string.ascii_lowercase[index] for index in data]
        return ''.join(a)

    def part_b(self):
        data = _next_password(self.answer_a)
        while not _is_valid(data):
            data = _next_password(data)
        a = [string.ascii_lowercase[index] for index in data]
        return ''.join(a)


def _next_password(password):
    password = password[-1::-1]
    for index, num in enumerate(password):
        if num == 25:
            password[index] = 0
        else:
            to_add = 1 + (num in [7, 13, 10])
            password[index] = num + to_add
            break
    return password[-1::-1]


def _is_valid(password):
    k = False
    o = zip(password, password[1:], password[2:])
    i = (z[0]-0 == z[1]-1 == z[2]-2 for z in o)
    k = any(i)

    counts = [len(list(b)) for a, b in itertools.groupby(password)]
    counts = [i >= 2 for i in counts]
    return (sum(counts) >= 2) and k
