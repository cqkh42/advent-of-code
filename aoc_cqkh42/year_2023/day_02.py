#!/usr/bin/python3
"""Solutions for day 2 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/2
"""
__all__ = ["Solution"]
from dataclasses import dataclass
from typing import Self
import re

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

import numpy as np
import parse


@dataclass
class Game:
    num: int
    cubes: np.array

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.num


PARSER = parse.compile(r"{:d} {:w}")
SHOW_SPLITTER = re.compile(r'[^:] (.*?);')


class Solution(BaseSolution):
    """Solutions for day 2 of 2018's Advent of Code."""
    def parse_line(self, line):
        game_num = int(re.findall(r'\d+', line)[0])
        l = re.sub(r'Game \d+: ', '', line)
        shows = l.split(';')
        shows = [{v: k for k, v in PARSER.findall(show)} for show in shows]
        k = np.array([
            [show.get(color, 0) for color in ['red', 'green', 'blue']]
            for show in shows
        ])
        return Game(game_num, k)

    def _process_data(self):
        return [self.parse_line(line) for line in self.lines]

    def part_a(self: Self) -> int:
        bag = np.array([12, 13, 14])
        return sum(
            game for game in self.processed
            if (game.cubes <= bag).all(axis=1).all()
        )

    def part_b(self: Self) -> int:
        return sum(
            np.product(game.cubes.max(axis=0)) for game in self.processed
        )


if __name__ == "__main__":
    submit_answers(Solution, 2, 2023)
