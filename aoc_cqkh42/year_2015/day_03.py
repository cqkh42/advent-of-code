#!/usr/bin/python3
"""Solutions for day 3 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/3
"""
__all__ = ["Solution"]
from collections.abc import Iterable
from typing import Self

import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def _unique_coords(steps: Iterable[Iterable[int, int]]) -> np.array:
    """Find unique coordinates given a list of steps in a path.

    Args:
        steps: Iterable of (x, y)

    Returns:
       numpy Array of unique coordinates visited.
    """
    coords = np.cumsum(steps, axis=0)
    return np.unique(coords, axis=0)


class Solution(BaseSolution):
    """Solutions for day 3 of 2015's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Number of unique coordinates in the path
        """
        return len(_unique_coords(self.processed))

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            Number of unique coordinates, assuming there are two
            paths zipped together.
        """
        santa = _unique_coords(self.processed[::2])
        robot = _unique_coords(self.processed[1::2])
        all_coords = np.concatenate((santa, robot))
        unique = np.unique(all_coords, axis=0)
        return len(unique)

    def _process_data(self: Self) -> np.array:
        """Turn glyphs into (x, y) steps.

        Returns:
            numpy Array of steps in (x, y) format
        """
        mapping_dict = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}
        return np.array(
            [[0, 0], *(mapping_dict[step] for step in self.input_)]
        )


if __name__ == "__main__":
    submit_answers(Solution, 3, 2015)
