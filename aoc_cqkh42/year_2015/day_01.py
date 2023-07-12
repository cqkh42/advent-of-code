#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/1
"""
__all__ = ["Solution"]

import itertools
from typing import Self

from more_itertools import first, iter_index

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 1 of 2015's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Difference in counts of '(' and ')'
        """
        return self.input_.count("(") - self.input_.count(")")

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            First index which brings cumsum equal to -1
        """
        positive = "("
        accumulated = itertools.accumulate(
            1 if item == positive else -1 for item in self.input_
        )
        indexes = iter_index(accumulated, -1)
        return first(indexes) + 1


if __name__ == "__main__":
    submit_answers(Solution, 1, 2015)
