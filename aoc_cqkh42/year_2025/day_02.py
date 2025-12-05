#!/usr/bin/python3
"""Solutions for day 2 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/2
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
    """Solutions for day 2 of 2025's Advent of Code."""
    PARSER = "{:d}-{:d}"

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        split = re.split(r"[-,]", self.input_)
        total = 0
        for start, end in more_itertools.chunked(split, 2):
            for num in range(int(start), int(end) + 1):
                string_num = str(num)
                try:
                    l, r = more_itertools.batched(string_num, len(string_num)//2, strict=True)
                    if l == r:
                        total += num
                except ValueError:
                    continue
        return total

    def part_b(self: Self) -> int:
        """Answer part b."""
        split = re.split(r"[-,]", self.input_)
        invalids = set()
        for start, end in more_itertools.chunked(split, 2):
            for num in range(int(start), int(end) + 1):
                string_num = str(num)
                for size in range(1, (len(string_num) // 2) + 1):
                    try:
                        groups = more_itertools.batched(string_num, size, strict=True)
                        if len(set(groups)) == 1:
                            invalids.add(num)
                    except ValueError:
                        continue
        return sum(invalids)





if __name__ == "__main__":
    submit_answers(Solution, 2, 2025)
