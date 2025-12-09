#!/usr/bin/python3
"""Solutions for day 7 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/7
"""
__all__ = ["Solution"]

import itertools
import math
from _pyrepl.commands import end

import networkx as nx
from typing import Self
import re
import more_itertools
from collections import defaultdict
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

FUNCS = {"*": math.prod, "+": sum}
class Solution(BaseSolution):
    """Solutions for day 7 of 2025's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        splitters = defaultdict(set)

        for index, row in enumerate(self.lines):
            splitters[index] = {col for col, value in enumerate(row) if value == "^"}
        rays = {self.lines[0].index("S")}
        tally = 0
        for line in splitters:
            new_rays = set()
            if not line:
                continue
            for ray in rays:
                if ray in splitters[line]:
                    tally += 1
                    new_rays.add(ray-1)
                    new_rays.add(ray+1)
                else:
                    new_rays.add(ray)
            rays = new_rays
        return tally

    def part_b(self: Self) -> int:
        """Answer part b."""
        splitters = defaultdict(set)
        rays = {num: defaultdict(int) for num in range(-1, len(self.lines))}

        for index, row in enumerate(self.lines):
            splitters[index] = {col for col, value in enumerate(row) if value == "^"}
        rays[-1][self.lines[0].index("S")] += 1
        for line in splitters:
            for ray, total in rays[line-1].items():
                if ray in splitters[line]:
                    rays[line][ray-1] += total
                    rays[line][ray+1] += total
                else:
                    rays[line][ray] += total
        return sum(rays[len(self.lines)-1].values())






if __name__ == "__main__":
    submit_answers(Solution, 7, 2025)
