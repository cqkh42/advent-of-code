#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/1
"""
__all__ = ["Solution"]

import itertools
from typing import Self

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 1 of 2018's Advent of Code."""

    def _parse(self: Self) -> list[int, ...]:
        return [int(num.strip('+')) for num in self.lines]

    def part_a(self: Self) -> int:
        return sum(self.parsed)

    def part_b(self: Self) -> int:
        seen = {0}
        current = 0
        for value in itertools.cycle(self.parsed):
            current += value
            if current in seen:
                return current
            seen.add(current)


if __name__ == "__main__":
    submit_answers(Solution, 1, 2018)
