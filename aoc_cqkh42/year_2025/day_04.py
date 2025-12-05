#!/usr/bin/python3
"""Solutions for day 4 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/4
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
    """Solutions for day 4 of 2025's Advent of Code."""
    PARSER = "{:d}-{:d}"

    def _parse(self) -> set[tuple[int, int]]:
        rolls = set()
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == "@":
                    rolls.add((x, y))
        return rolls
    def part_a(self: Self) -> int:
        """Answer part a.
        """
        total = 0
        for x, y in self.parsed:
            options = {
                (x+1, y), (x+1, y-1), (x+1, y+1), (x-1, y), (x-1, y+1), (x-1, y-1), (x, y+1), (x, y-1)
            }
            total += len(options.intersection(self.parsed)) < 4
        return total

    def part_b(self: Self) -> int:
        """Answer part b."""
        total = 0
        for _ in range(35):
            queue = list(self.parsed)
            for x, y in queue:
                if (x, y) not in self.parsed:
                    continue
                options = {
                    (x + 1, y), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1), (x, y + 1),
                    (x, y - 1)
                }
                if len(options.intersection(self.parsed)) < 4:
                    self.parsed.remove((x,y))
                    total += 1
        return total



if __name__ == "__main__":
    submit_answers(Solution, 4, 2025)
