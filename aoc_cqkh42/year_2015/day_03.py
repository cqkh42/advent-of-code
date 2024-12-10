#!/usr/bin/python3
"""Solutions for day 3 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/3
"""
__all__ = ["Solution"]
from collections.abc import Iterable
import itertools
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.coords import Coords


#todo compass coords

def _unique_coords(steps: Iterable[Iterable[int, int]]) -> set[Coords]:
    """Find unique coordinates given a list of steps in a path.

    Args:
        steps: Iterable of (x, y)

    Returns:
       numpy Array of unique coordinates visited.
    """
    return set(itertools.accumulate(steps))


class Solution(BaseSolution):
    """Solutions for day 3 of 2015's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Number of unique coordinates in the path
        """
        return len(_unique_coords(self.parsed))

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            Number of unique coordinates, assuming there are two
            paths zipped together.
        """
        santa = _unique_coords(self.parsed[::2])
        robot = _unique_coords(self.parsed[1::2])
        santa.update(robot)
        return len(santa)

    def _parse(self: Self) -> list[Coords]:
        """Turn glyphs into (x, y) steps.

        Returns:
            numpy Array of steps in (x, y) format
        """
        mapping_dict = {">": Coords(1, 0), "<": Coords(-1, 0), "^": Coords(0, -1), "v": Coords(0, 1)}
        return [Coords(0, 0), *(mapping_dict[step] for step in self.input_)]


if __name__ == "__main__":
    submit_answers(Solution, 3, 2015)
