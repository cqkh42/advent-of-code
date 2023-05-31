import itertools
import re

TWO_REGEX = re.compile(r'(\d)\1')

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        start, end = self.data.split('-')
        return sum(
            _is_valid(password) for password in range(int(start), int(end)))

    def part_b(self):
        start, end = self.data.split('-')
        only_twice = (
            password for password in range(int(start), int(end))
            if _repeats_once(password)
        )
        return sum(_is_valid(password) for password in only_twice)


def _repeats_once(password):
    grouped = itertools.groupby(str(password))
    counts = (len(list(group)) for _, group in grouped)
    two_counts = (count == 2 for count in counts)
    return any(two_counts)


def _is_valid(password):
    str_pass = str(password)
    duplicates = bool(TWO_REGEX.search(str_pass))
    increases = all(left <= right for left, right in zip(str_pass, str_pass[1:]))
    return increases and duplicates
