#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/1
"""
__all__ = ["Solution"]

import itertools
from typing import Self

from aocd.models import Puzzle
from more_itertools import first, iter_index

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 1 of 2015's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Difference in counts of '(' and ')'
        """
        return self.data.count("(") - self.data.count(")")

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            First index which brings cumsum equal to -1
        """
        positive = "("
        accumulated = itertools.accumulate(
            1 if item == positive else -1 for item in self.data
        )
        indexes = iter_index(accumulated, -1)
        return first(indexes) + 1

    def _parse_data(self: Self) -> str:
        return self.data


def main() -> None:
    """Solve and submit answers for 2015 day 1."""
    puzzle = Puzzle(year=2015, day=1)
    solution = Solution(puzzle.input_data)
    puzzle.answer_a = solution.part_a()
    puzzle.answer_b = solution.part_b()


if __name__ == "__main__":
    main()
