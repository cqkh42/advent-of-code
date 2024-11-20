#!/usr/bin/python3
"""Solutions for day 8 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/8
"""
__all__ = ["Solution"]
import re
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 8 of 2015's Advent of Code."""

    def part_a(self: Self) -> int:
        """Answer part a.

        Returns:
            Number of characters of code for string literals minus
            number of characters for the values of the strings
        """
        return len(self.input_) - len(self.lines) + 1 - sum(self.parsed_lines)

    def part_b(self: Self) -> int:
        """Answer part b.

        Returns:
            2 * number of lines + number of " + number of \
        """
        return 2 * len(self.lines) + self.input_.count('"') + self.input_.count("\\")

    def _parse_line(self, line: str):
        replacements = [
            (r'^"', ""),
            (r'"$', ""),
            (r"\\\\", r"\\"),
            (r'\\"', '"'),
            (r"\\x[a-f0-9]{2}", "x"),
        ]
        for regex, repl in replacements:
            line = re.sub(regex, repl, line)
        return len(line)


if __name__ == "__main__":
    submit_answers(Solution, 8, 2015)
