#!/usr/bin/python3
"""Solutions for day 1 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/1
"""
__all__ = ["Solution"]

import itertools
from typing import Self

from more_itertools import first, iter_index

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 1 of 2025's Advent of Code."""
    parsed_lines: list[int]

    def _parse_line(self, line: str) -> int:
        if line.startswith("L"):
            string = f"-{line[1:]}"
        else:
            string = line[1:]
        num = int(string)
        return num


    def part_a(self: Self) -> int:
        """Answer part a.
        """
        current = 50
        tally = 0
        for num in self.parsed_lines:
            new = current + num
            _, mod = divmod(new, 100)
            tally += mod == 0
            current = mod
        return tally

    def part_b(self: Self) -> int:
        """Answer part b.
        """
        visited = [50]
        for num in self.parsed_lines:
            current = visited[-1]
            if num > 0:
                visited.extend(range(current+1, current+num+1))
            else:
                visited.extend(range(current - 1, current + num - 1, -1))
        return sum(not(num % 100) for num in visited)



if __name__ == "__main__":
    submit_answers(Solution, 1, 2025)
