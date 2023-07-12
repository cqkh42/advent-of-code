#!/usr/bin/python3
"""Solutions for day 4 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/4
"""
__all__ = ["Solution"]
import itertools
from hashlib import md5
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 4 of 2015's Advent of Code."""

    _counter = itertools.count()

    def _crack_hash(self: Self, sequence: str) -> int:
        for answer in self._counter:
            hash_ = self.processed.copy()
            hash_.update(f"{answer}".encode())
            if hash_.hexdigest().startswith(sequence):
                break
        return answer

    def _process_data(self: Self) -> md5:
        return md5(self.input_.encode())

    def part_a(self: Self) -> int:
        answer = self._crack_hash("0" * 5)
        return answer

    def part_b(self: Self) -> int:
        return self._crack_hash("0" * 6)


if __name__ == "__main__":
    submit_answers(Solution, 4, 2015)
