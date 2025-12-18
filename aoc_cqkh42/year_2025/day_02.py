#!/usr/bin/python3
"""Solutions for day 2 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/2
"""
__all__ = ["Solution"]

import itertools
from typing import Self, Any
import more_itertools
from more_itertools import first, iter_index
import re
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import functools

class Solution(BaseSolution):
    """Solutions for day 2 of 2025's Advent of Code."""
    PARSER = "{:d}-{:d}"

    simples = set()

    def _parse(self: Self) -> Any:
        nums = []
        for start, end in more_itertools.chunked(self.numbers, 2):
            nums.extend(range(start, abs(end) + 1))
        return nums

    @functools.cache
    def part_a(self: Self) -> int:
        """Answer part a.
        """
        regex = re.compile(r"^(\d+)\1$", flags=re.MULTILINE)
        s = "\n".join([str(i) for i in self.parsed])
        print(s[:20])
        k = regex.findall(s)
        return sum(int(num) for num in k)
        print(k[:5])
        self.simples = {num for num in self.parsed if regex.match(str(num))}
        return sum(self.simples)

    def part_b(self: Self) -> int:
        """Answer part b."""
        regex = re.compile(r"^(\d+)\1+$")
        k = {num for num in set(self.parsed).difference(self.simples) if regex.match(str(num))}

        return sum(k) + self.part_a()





if __name__ == "__main__":
    submit_answers(Solution, 2, 2025)
