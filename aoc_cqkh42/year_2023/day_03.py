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

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import numpy as np
import parse


@dataclass
class Number:
    num: int
    y: int
    x_min: int
    x_max: int

    def above(self):
        return max(0, self.x_min-1), min(139, self.x_max+1)

    def above_new(self):
        return slice(max(0, self.x_min-1), min(139, self.x_max+1))

    def below(self):
        return max(0, self.x_min - 1), min(139, self.x_max + 1)

    def left(self):
        if self.x == 0:
            yield

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
            found = list(num_regex.finditer(line))
            line_numbers = [Number(int(num.group()), int(y), *num.span()) for
                            num in found]
            numbers.extend(line_numbers)
        return numbers

    def valid_slice(self, y, x_slice):
        if not 0 <= y <= 139:
            return False
        if x_slice.start < 0:
            return False
        if x_slice.stop > 140: return False
        valid = self.lines[y][x_slice]
        valid = (not i.isnumeric() and not i == '.' for i in valid)
        return any(valid)

    def star_in_slice(self):



    def part_a(self: Self) -> int:
        return sum(num for num in self.processed if (
            self.valid_slice(num.y - 1, num.above_new()) or
            self.valid_slice(num.y + 1, num.above_new()) or
            self.valid_slice(num.y, slice(num.x_min - 1, num.x_min)) or
            self.valid_slice(num.y, slice(num.x_max, num.x_max + 1))
        ))

    def part_b(self: Self) -> int:
        gears = defaultdict(list)
        for num in self.processed:
            if num.y != 0:
                k = num.above()
                valid = self.lines[num.y-1][k[0]: k[1]]
                valid = [index for index, value in enumerate(valid, k[0]) if value == '*']
                for x in valid:
                    gears[(num.y-1, x)].append(num)
            if num.y != 139:
                k = num.above()
                valid = self.lines[num.y + 1][k[0]: k[1]]
                valid = [index for index, value in enumerate(valid, k[0]) if
                         value == '*']
                for x in valid:
                    gears[(num.y + 1, x)].append(num)
            if num.x_min != 0:
                valid = self.lines[num.y][num.x_min-1]
                if valid == '*':
                    gears[num.y, num.x_min-1].append(num)
            if num.x_max != 140:
                valid = self.lines[num.y][num.x_max]
                if valid == '*':
                    gears[num.y, num.x_max].append(num)
        return sum(np.prod(nums) for nums in gears.values() if len(nums) == 2)


if __name__ == "__main__":
    submit_answers(Solution, 2, 2023)
