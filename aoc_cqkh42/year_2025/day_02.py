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

@functools.cache
def find_divisors_simple(n):
    divisors = [i for i in range(1, (n //2)+1) if n % i == 0]
    return divisors

def is_splitable(num):
    for size in find_divisors_simple(len(num)):
        groups = more_itertools.batched(num, size)
        if len(set(groups)) == 1:
            return True
class Solution(BaseSolution):
    """Solutions for day 2 of 2025's Advent of Code."""
    PARSER = "{:d}-{:d}"

    simples = set()

    def _parse(self: Self) -> Any:
        nums = []
        split = re.split(r"[-,]", self.input_)
        for start, end in more_itertools.chunked(split, 2):
            nums.extend(range(int(start), int(end) + 1))
        return set(nums)

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        for num in self.parsed:
            try:
                l, r = more_itertools.batched(str(num), len(str(num))//2, strict=True)
                if l == r:
                    self.simples.add(num)
            except ValueError:
                continue
        return sum(self.simples)

    def part_b(self: Self) -> int:
        """Answer part b."""
        invalids = 0
        for num in self.parsed:
            if is_splitable(str(num)):
                invalids+=num

        return (invalids)





if __name__ == "__main__":
    submit_answers(Solution, 2, 2025)
