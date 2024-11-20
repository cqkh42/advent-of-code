#!/usr/bin/python3
"""Solutions for day 3 of 2018's Advent of Code.

Read the full puzzle at https://adventofcode.com/2018/day/3
"""
__all__ = ["Solution"]

import itertools
import collections
from dataclasses import dataclass
from typing import Self
from functools import cached_property

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import parse

parser = parse.compile(r'#{:d} @ {:d},{:d}: {:d}x{:d}')
@dataclass
class Claim:
    claim: int
    left: int
    top: int
    width: int
    height: int

    @cached_property
    def squares(self) -> set[tuple[int, int]]:
        x_range = range(self.left, self.left+self.width)
        y_range = range(self.top, self.top +self.height)
        return set(itertools.product(x_range, y_range))


class Solution(BaseSolution):
    """Solutions for day 3 of 2018's Advent of Code."""

    def _parse(self: Self) -> list[Claim]:
        return [Claim(*row) for row in parser.findall(self.input_)]

    @cached_property
    def counter(self):
        k = list(more_itertools.flatten(
            claim.squares for claim in self.parsed))
        return collections.Counter(k)

    def part_a(self: Self) -> int:
        return sum(i > 1 for i in self.counter.values())

    def part_b(self: Self) -> str:
        c = {a for a, b in self.counter.items() if b == 1}
        for claim in self.parsed:
            if claim.squares.issubset(c):
                return claim.claim





if __name__ == "__main__":
    submit_answers(Solution, 2, 2018)
