#!/usr/bin/python3
"""Solutions for day 5 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/5
"""
__all__ = ["Solution"]
import re
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 5 of 2015's Advent of Code."""

    repeating_char = re.compile(r"(\w)\1")
    repeating_chars = re.compile(r"(\w{2}).*\1")
    repeats_with_space = re.compile(r"(\w).\1")
    bad_phrases = ("ab", "cd", "pq", "xy")

    def _is_nice_a(self: Self, string: str) -> bool:
        vowel_count = sum(string.count(vowel) for vowel in "aeiou")
        has_repeating_char = bool(self.repeating_char.search(string))
        no_bad_phrases = all(phrase not in string for phrase in self.bad_phrases)
        return vowel_count >= 3 and has_repeating_char and no_bad_phrases

    def _is_nice_b(self: Self, string: str) -> bool:
        repeats = bool(self.repeating_chars.search(string))
        one_between = bool(self.repeats_with_space.search(string))
        return repeats and one_between

    def part_a(self: Self) -> int:
        return sum(self._is_nice_a(string) for string in self.lines)

    def part_b(self: Self) -> int:
        return sum(self._is_nice_b(string) for string in self.lines)


if __name__ == "__main__":
    submit_answers(Solution, 5, 2015)
