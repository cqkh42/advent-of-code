#!/usr/bin/python3
"""Solutions for day 2 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/2
"""
__all__ = ["Solution"]

import itertools
import math

from typing import Self, Any

import more_itertools
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Present(list):
    """A present represented by 3 dimensions.

    Attributes:
        paper: How much paper is needed for the present.
        ribbon: How much ribbon is needed for the present.
    """
    def _pairs(self: Self) -> itertools.combinations:
        """Pairs of dimensions.

        Returns:
            generator: iterable of pairs of dimensions
        """
        return itertools.combinations(self, 2)

    @property
    def paper(self: Self) -> int:
        """How much paper is needed for the present.

        Returns:
            int: the amount of paper needed for the present
        """
        sides = [math.prod(corner) for corner in self._pairs()]
        return min(sides) + sum(sides) * 2

    @property
    def ribbon(self: Self) -> int:
        """How much ribbon is needed for the present.

        Returns:
            int: the amount of ribbon needed for the present
        """
        perms = (sum(corner) for corner in self._pairs())
        return min(perms) * 2 + math.prod(self)


class Solution(BaseSolution):
    """Solutions for day 2 of 2015's Advent of Code."""
    def _parse(self):
        return self.line_numbers_as(Present)

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Total paper needed for all presents
        """
        return sum(present.paper for present in self.parsed)

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            Total ribbon needed for all presents
        """
        return sum(present.ribbon for present in self.parsed)


if __name__ == "__main__":
    submit_answers(Solution, 2, 2015)
