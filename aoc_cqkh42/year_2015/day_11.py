import itertools
import re
import string

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return [string.ascii_lowercase.index(char) for char in self.data]

    def part_a(self):
        return self.next_valid_password()

    def part_b(self):
        return self.next_valid_password()

    def cycle_password(self):
        password = self.parsed_data[::-1]
        for index, num in enumerate(password):
            if num == 25:
                password[index] = 0
            else:
                password[index] = num + 1 + (num in [7, 13, 10])
                break
        self.parsed_data = password[::-1]

    def next_valid_password(self):
        self.cycle_password()
        while not _is_valid(self.parsed_data):
            self.cycle_password()
        a = [string.ascii_lowercase[index] for index in self.parsed_data]
        return ''.join(a)


def _is_valid(password):
    # TODO this is messy
    triples = zip(password, password[1:], password[2:])
    k = any(first == second-1 == third-2 for first, second, third in triples)

    counts = [len(list(b)) for a, b in itertools.groupby(password)]
    counts = [i >= 2 for i in counts]
    return (sum(counts) >= 2) and k
