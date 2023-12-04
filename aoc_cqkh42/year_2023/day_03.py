#!/usr/bin/python3
"""Solutions for day 3 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/3
"""
__all__ = ["Solution"]

import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import Self
import re

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import numpy as np


@dataclass
class Number:
    num: int
    y: int
    x_min: int
    x_max: int

    def x_span(self):
        return slice(max(0, self.x_min-1), min(139, self.x_max+1))

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.num * other.num

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.num


class Solution(BaseSolution):
    """Solutions for day 3 of 2018's Advent of Code."""
    def _process_data(self: Self) -> list[Number, ...]:
        num_regex = re.compile(r'(\d+)')
        numbers = []
        for y, line in enumerate(self.lines):
            line_numbers = [
                Number(int(num.group()), y, *num.span())
                for num in num_regex.finditer(line)
            ]
            numbers.extend(line_numbers)
        return numbers

    def valid_slice(self, y, x_slice):
        if not 0 <= y <= 139 or x_slice.start < 0 or x_slice.stop > 140:
            return False
        valid = self.lines[y][x_slice]
        valid = (not i.isnumeric() and not i == '.' for i in valid)
        return any(valid)

    def find_stars(self, y, x_slice):
        if not 0 <= y <= 139 or x_slice.start < 0 or x_slice.stop > 140:
            yield from []
        else:
            valid = self.lines[y][x_slice]
            yield from [
                (y, index) for index, value in enumerate(valid, x_slice.start) if
                value == '*'
            ]

    def part_a(self: Self) -> int:
        return sum(num for num in self.processed if (
                self.valid_slice(num.y - 1, num.x_span()) or
                self.valid_slice(num.y + 1, num.x_span()) or
                self.valid_slice(num.y, slice(num.x_min - 1, num.x_min)) or
                self.valid_slice(num.y, slice(num.x_max, num.x_max + 1))
        ))

    def part_b(self: Self) -> int:
        gears = defaultdict(list)
        for num in self.processed:
            around = (
                self.find_stars(num.y - 1, num.x_span()),
                self.find_stars(num.y + 1, num.x_span()),
                self.find_stars(num.y, slice(num.x_min - 1, num.x_min)),
                self.find_stars(num.y, slice(num.x_max, num.x_max + 1))
            )
            for coords in more_itertools.flatten(around):
                gears[coords].append(num)

        return sum(np.prod(nums) for nums in gears.values() if len(nums) == 2)


if __name__ == "__main__":
    submit_answers(Solution, 3, 2023)
