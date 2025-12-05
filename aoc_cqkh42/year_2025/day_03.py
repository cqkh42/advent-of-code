#!/usr/bin/python3
"""Solutions for day 3 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/3
"""
__all__ = ["Solution"]

import itertools
from typing import Self
import more_itertools
from more_itertools import first, iter_index
import re
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution



class Solution(BaseSolution):
    """Solutions for day 3 of 2025's Advent of Code."""
    PARSER = "{:d}-{:d}"

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        total = 0
        for line in self.lines:
            maxed = max(line[:-1])
            index = line.index(maxed)
            maxed += max(line[index+1:])
            total += int(maxed)
        return total

    def part_b(self: Self) -> int:
        """Answer part b."""
        total = 0
        for line in self.lines:
            first = max(line[:-11])
            index = line.index(first)
            line = line[index+1:]
            for num in range(11):
                if num != 10:
                    val = max(line[:-(10-num)])
                else:
                    val = max(line)
                index = line.index(val)
                line = line[index+1:]
                first += val
            total += int(first)

        return total









if __name__ == "__main__":
    submit_answers(Solution, 3, 2025)
