#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2016/day/8
"""
__all__ = ["Solution"]

import itertools
from typing import Self

import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.aocr import word
from aoc_cqkh42.helpers.base_solution import BaseSolution

RECTANGLE_PARSER = parse.compile("rect {:d}x{:d}")  # noqa: P103
ROW_PARSER = parse.compile("rotate row y={:d} by {:d}")  # noqa: P103
COL_PARSER = parse.compile("rotate column x={:d} by {:d}")  # noqa: P103


class Solution(BaseSolution):
    """Solutions for day 8 of 2016's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Count of 'lit' pixels
        """
        return self.processed.sum()

    def part_b(self: Self) -> str:
        """Answer part a.

        Returns:
            Word spelled by the pixels
        """
        return word(itertools.chain.from_iterable(self.processed))

    def _process_data(self: Self) -> np.array:
        """Create the post-processed screen.

        Returns:
            screen where 1 indicates a lit pixel
        """
        screen = np.zeros((6, 50))
        for instruction in self.lines:
            if match := RECTANGLE_PARSER.parse(instruction):
                x_size, y_size = match
                screen[:y_size, :x_size] = 1
            elif match := ROW_PARSER.parse(instruction):
                y_size, steps = match
                screen[y_size] = np.roll(screen[y_size], steps)
            else:
                x_size, steps = COL_PARSER.parse(instruction)
                screen[:, x_size] = np.roll(screen[:, x_size], steps)

        return screen.astype(int)


if __name__ == "__main__":
    submit_answers(Solution, 8, 2016)
