#!/usr/bin/python3
"""Solutions for day 18 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/18
"""
__all__ = ["Solution"]
from typing import Self

import numpy as np
from scipy.ndimage import generic_filter

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

#todo as array?

def _iteration(lights):
    f = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    neighbours = generic_filter(
        lights, lambda x: x.sum(), footprint=f, mode="constant", output=int
    )
    threes = neighbours == 3
    two_or_three = (neighbours == 2) | threes
    stays_on = lights & two_or_three
    turns_on = threes & ~lights
    lights = stays_on | turns_on
    return lights


class Solution(BaseSolution):
    """Solutions for day 18 of 2015's Advent of Code."""

    def _parse(self: Self) -> np.ndarray[bool]:
        return np.array(self.lines_as(list)) == '#'

    def part_a(self: Self, steps: int = 100) -> int:
        light_arr = self.parsed.copy()
        for _ in range(steps):
            light_arr = _iteration(light_arr)
        return light_arr.sum()

    def part_b(self: Self, steps: int = 100) -> int:
        light_arr = self.parsed
        light_arr[[0, 0, -1, -1], [0, -1, 0, -1]] = 1

        for _ in range(steps):
            light_arr = _iteration(light_arr)
            light_arr[[0, 0, -1, -1], [0, -1, 0, -1]] = 1
        return light_arr.sum()


if __name__ == "__main__":
    submit_answers(Solution, 18, 2015)
