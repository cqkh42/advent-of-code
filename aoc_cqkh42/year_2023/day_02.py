#!/usr/bin/python3
"""Solutions for day 2 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/2
"""
__all__ = ["Solution"]

import re
from typing import Self

import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


PARSER = parse.compile(r"{:d} {:w}")
SHOW_SPLITTER = re.compile(r'[^:] (.*?);')


def parse_line(line):
    shows = [
        {color: num for num, color in PARSER.findall(show)}
        for show in re.sub(r'Game \d+: ', '', line).split(';')
    ]
    return np.array([
        [show.get(color, 0) for color in ['red', 'green', 'blue']]
        for show in shows
    ])


class Solution(BaseSolution):
    """Solutions for day 2 of 2023's Advent of Code."""

    def _parse(self):
        return [parse_line(line) for line in self.lines]

    def part_a(self: Self) -> int:
        bag = np.array([12, 13, 14])
        return sum(
            index for index, game in enumerate(self.parsed, 1)
            if (game <= bag).all(axis=1).all()
        )

    def part_b(self: Self) -> int:
        return sum(
            np.product(game.max(axis=0)) for game in self.parsed
        )


if __name__ == "__main__":
    submit_answers(Solution, 2, 2023)
