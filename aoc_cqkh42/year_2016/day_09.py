#!/usr/bin/python3
"""Solutions for day 9 of 2016's Advent of Code.

Read the full puzzle at https://adventofcode.com/2016/day/9
"""
__all__ = ["Solution"]
import re
from collections import defaultdict
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def expand_string(right: str, left: str = "") -> str:
    if "(" not in right:
        return left + right
    else:
        to_left, chars, count, new_right = re.split(BRACKET_REGEX, right, 1)
        left += to_left + new_right[: int(chars)] * int(count)
        right = new_right[int(chars) :]
        return expand_string(right, left)


def deep_expansion(counts: dict[str, int], total: int) -> int:
    if not counts:
        return total
    new_counts = defaultdict(int)
    for string, count in counts.items():
        if "(" not in string:
            total += count * len(string)
            continue
        if k := string.index("("):
            total += count * k
            new_counts[string[k:]] += count
            continue
        _, num_chars, b, rest = re.split(BRACKET_REGEX, string, 1)
        sl_left, sl_right = rest[: int(num_chars)], rest[int(num_chars) :]
        new_counts[sl_left] += int(b) * count
        new_counts[sl_right] += count

    return deep_expansion(new_counts, total)


class Solution(BaseSolution):
    def part_a(self: Self) -> int:
        return len(expand_string(self.input_))

    def part_b(self: Self) -> int:
        c = {self.input_: 1}
        return deep_expansion(c, 0)


BRACKET_REGEX = re.compile(r"\((\d+)+x(\d+)\)")


if __name__ == "__main__":
    submit_answers(Solution, 9, 2016, "github")
