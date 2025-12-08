#!/usr/bin/python3
"""Solutions for day 6 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/6
"""
__all__ = ["Solution"]

import itertools
import math
from typing import Self
import re
import more_itertools
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

FUNCS = {"*": math.prod, "+": sum}
class Solution(BaseSolution):
    """Solutions for day 6 of 2025's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        transposed = zip(*self.line_numbers)
        last = re.split(r"\s+", self.lines[-1].strip())
        return sum(FUNCS[symbol](nums) for nums, symbol in zip(transposed, last))

    def part_b(self: Self) -> int:
        """Answer part b."""
        last = re.split(r"\s+", self.lines[-1].strip())
        transposed = ["".join(num).strip() for num in zip(*self.lines[:-1])]
        transposed = more_itertools.split_at(transposed, lambda num: not num)
        total = 0
        for nums, symbol in zip(transposed, last):
            nums = [int(num) for num in nums]
            total += FUNCS[symbol](nums)
        return total





if __name__ == "__main__":
    submit_answers(Solution, 6, 2025)
