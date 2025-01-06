import itertools
import re
from typing import Self, Any

TWO_REGEX = re.compile(r'(\d)\1')

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        a, b = self.input_.split('-')
        return int(a), int(b)
    def part_a(self):
        return sum(
            _is_valid(password) for password in range(*self.parsed))

    def part_b(self):
        only_twice = (
            password for password in range(*self.parsed)
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
