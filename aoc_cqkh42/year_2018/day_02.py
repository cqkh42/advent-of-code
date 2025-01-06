#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/1
"""
__all__ = ["Solution"]

import itertools
import collections
from typing import Self

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 2 of 2018's Advent of Code."""
    def _parse_line(self, line: str):
        return line, collections.Counter(line)

    def _parse(self: Self) -> dict[str, collections.Counter]:
        return dict(self.parsed_lines)

    def part_a(self: Self) -> int:
        a = len([a for a in self.parsed.values() if 2 in a.values()])
        b = len([i for i in self.parsed.values() if 3 in i.values()])
        return a*b

    def part_b(self: Self) -> str:
        for a, b in itertools.combinations(self.lines, 2):
            replaced = ''.join(z for z, y in zip(a, b) if z == y)
            if len(replaced) == len(self.lines[0]) - 1:
                return replaced




if __name__ == "__main__":
    submit_answers(Solution, 2, 2018)
