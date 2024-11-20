#!/usr/bin/python3
"""Solutions for day 3 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/3
"""
__all__ = ["Solution"]

import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Self

import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Number:
    num: int
    y: int
    x_min: int
    x_max: int

    def x_span(self):
        return slice(max(0, self.x_min - 1), min(139, self.x_max + 1))

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.num * other.num

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.num


class Solution(BaseSolution):
    """Solutions for day 3 of 2018's Advent of Code."""

    def _parse(self: Self) -> list[Number, ...]:
        num_regex = re.compile(r'(\d+)')
        numbers = []
        for y, line in enumerate(self.lines):
            line_numbers = [
                Number(int(num.group()), y, *num.span())
                for num in num_regex.finditer(line)
            ]
            numbers.extend(line_numbers)
        return numbers

    def _validate(self, y, x_slice):
        if not 0 <= y <= 139 or x_slice.start < 0 or x_slice.stop > 140:
            return []
        k = self.lines[y][x_slice]
        return [(y, index) for index, i in enumerate(k, x_slice.start) if not i.isnumeric() and not i == '.']

    def _validate_2(self, num):
        for y, span in (
                (num.y - 1, num.x_span()),
                (num.y + 1, num.x_span()),
                (num.y, slice(num.x_min - 1, num.x_min)),
                (num.y, slice(num.x_max, num.x_max + 1))
        ):
            yield from self._validate(y, span)

    def part_a(self: Self) -> int:
        return sum(
            num for num in self.parsed if any(self._validate_2(num))
        )

    def part_b(self: Self) -> int:
        gears = defaultdict(list)
        for num in self.parsed:
            for coords in self._validate_2(num):
                gears[coords].append(num)
        return sum(np.prod(nums) for nums in gears.values() if len(nums) == 2)


if __name__ == "__main__":
    submit_answers(Solution, 3, 2023)
