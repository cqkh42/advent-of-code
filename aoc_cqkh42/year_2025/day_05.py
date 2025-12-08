#!/usr/bin/python3
"""Solutions for day 5 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/5
"""
__all__ = ["Solution"]

import itertools
from typing import Self
import more_itertools
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def flatten_ranges(ranges):
    new_ranges = []
    sorted_ = sorted(ranges, key=lambda range_: (range_.start, range_.stop))
    while sorted_:
        first = sorted_[0]
        try:
            second = sorted_[1]
        except IndexError:
            new_ranges.append(first)
            return new_ranges
        else:
            if second.start in first or second.start == first.stop:
                new_ranges.append(range(first.start, max(second.stop, first.stop)))
                sorted_ = sorted_[2:]
            elif second.start < first.stop:
                raise
            else:
                new_ranges.append(first)
                sorted_ = sorted_[1:]
    return new_ranges
class Solution(BaseSolution):
    """Solutions for day 5 of 2025's Advent of Code."""
    PARSER = "{:d}-{:d}"

    def _parse(self) -> tuple[list[range], list[int]]:
        ranges, nums = more_itertools.split_at(self.lines, lambda line: not line)
        ranges = [range_.split("-") for range_ in ranges]
        ranges = [range(int(start), int(end)+1) for start, end in ranges]

        nums = [int(num) for num in nums]

        return ranges, nums

    def is_fresh(self, num):
        return any(num in range_ for range_ in self.parsed[0])

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        ranges, nums = self.parsed
        return sum(self.is_fresh(num) for num in nums)



    def part_b(self: Self) -> int:
        """Answer part b."""
        ranges = self.parsed[0]
        for _ in range(4):
            ranges = flatten_ranges(ranges)
        return sum(len(range_) for range_ in ranges)






if __name__ == "__main__":
    submit_answers(Solution, 5, 2025)
