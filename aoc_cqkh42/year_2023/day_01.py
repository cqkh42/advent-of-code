#!/usr/bin/python3
"""Solutions for day 1 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/1
"""
__all__ = ["Solution"]

from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def _parse_string(string, include_strings=True):
    mapping = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    nums = []
    slices = [string[start:] for start in range(len(string))]
    for sliced in slices:
        if sliced[0].isdigit():
            nums.append(sliced[0])
            continue
        if include_strings:
            for string_val, num in mapping.items():
                if sliced.startswith(string_val):
                    nums.append(num)
                    continue
    return int(f'{nums[0]}{nums[-1]}')


class Solution(BaseSolution):
    """Solutions for day 1 of 2018's Advent of Code."""

    def part_a(self: Self) -> int:
        return sum(_parse_string(line, False) for line in self.lines)

    def part_b(self: Self) -> int:
        return sum(_parse_string(line) for line in self.lines)


if __name__ == "__main__":
    submit_answers(Solution, 1, 2023)
