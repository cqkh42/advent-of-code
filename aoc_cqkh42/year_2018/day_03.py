#!/usr/bin/python3
"""Solutions for day 3 of 2018's Advent of Code.

Read the full puzzle at https://adventofcode.com/2018/day/3
"""
__all__ = ["Solution"]

import itertools
import collections
from collections import Counter
from dataclasses import dataclass
from typing import Self
from functools import cached_property

import more_itertools
from more_itertools.more import first

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import parse


# @dataclass
class Claim:
    PARSER = parse.compile(
        r'#{claim:d} @ {left:d},{top:d}: {width:d}x{height:d}')
    def __init__(self, data):
        data = self.PARSER.search(data)
        self.claim = data['claim']
        self.left = data['left']
        self.top = data['top']
        self.width = data['width']
        self.height = data['height']

    @cached_property
    def squares(self) -> set[tuple[int, int]]:
        x_range = range(self.left, self.left+self.width)
        y_range = range(self.top, self.top +self.height)
        return set(itertools.product(x_range, y_range))


class Solution(BaseSolution):
    """Solutions for day 3 of 2018's Advent of Code."""
    @cached_property
    def counter(self) -> Counter:
        k = list(more_itertools.flatten(
            claim.squares for claim in self.lines_as(Claim)))
        return collections.Counter(k)

    def part_a(self: Self) -> int:
        return sum(count > 1 for count in self.counter.values())

    def part_b(self: Self) -> str:
        c = {claim for claim in self.counter if self.counter[claim] == 1}
        return first(
            claim.claim for claim in self.lines_as(Claim)
            if claim.squares.issubset(c)
        )


if __name__ == "__main__":
    submit_answers(Solution, 2, 2018)
