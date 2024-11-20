#!/usr/bin/python3
#todo hash
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

    _salt = itertools.count()

    def _crack_hash(self: Self, sequence: str) -> int:
        """Iterate through salts until the hash's hex ends in `sequence`

        Args:
            sequence: str that the hex should end in

        Returns:
            int that creates a hash ending in `sequence`
        """
        for answer in self._salt:
            hash_ = self.processed.copy()
            hash_.update(f"{answer}".encode())
            if hash_.hexdigest().startswith(sequence):
                return answer
        return self._salt

    def _process_data(self: Self) -> md5:
        """Create a md5 of the input data.

        Returns:
            md5 of the input data
        """
        return md5(self.input_.encode())

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            First int that creates a hash ending in 5 zeroes.
        """
        answer = self._crack_hash("0" * 5)
        return answer

    def part_b(self: Self) -> int:
        """Answer part a.

        Returns:
            First int that creates a hash ending in 6 zeroes.
        """
        return self._crack_hash("0" * 6)


if __name__ == "__main__":
    submit_answers(Solution, 4, 2015)
