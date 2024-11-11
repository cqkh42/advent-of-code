#!/usr/bin/python3
"""Solutions for day 2 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/2
"""
__all__ = ["Solution"]

import itertools
import math
from dataclasses import dataclass
from typing import Self

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Present:
    """A present represented by 3 dimensions.

    Attributes:
        dim_0: The first dimension
        dim_1: The second dimension
        dim_2: The third dimension
        paper: How much paper is needed for the present.
        ribbon: How much ribbon is needed for the present.
    """

    dim_0: int
    dim_1: int
    dim_2: int

    def _pairs(self: Self) -> itertools.combinations:
        """Pairs of dimensions.

        Returns:
            generator: iterable of pairs of dimensions
        """
        return itertools.combinations([self.dim_0, self.dim_1, self.dim_2], 2)

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
        return min(perms) * 2 + math.prod([self.dim_0, self.dim_1, self.dim_2])


class Solution(BaseSolution):
    """Solutions for day 2 of 2015's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Total paper needed for all presents
        """
        return sum(present.paper for present in self.processed)

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            Total ribbon needed for all presents
        """
        return sum(present.ribbon for present in self.processed)

    def _process_data(self: Self) -> list[Present]:
        """Build a list of Presents from raw input data.

        Returns:
            List of Presents
        """
        parser = parse.compile("{dim_0:d}x{dim_1:d}x{dim_2:d}")

        return [
            Present(dims["dim_0"], dims["dim_1"], dims["dim_2"])
            for dims in parser.findall(self.input_)
        ]


if __name__ == "__main__":
    submit_answers(Solution, 2, 2015)
