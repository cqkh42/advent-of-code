#!/usr/bin/python3
"""Solutions for day 9 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/9
"""
__all__ = ["Solution"]

import itertools
import math
import shapely

import networkx as nx
from typing import Self, Any
import re
import more_itertools
from dataclasses import dataclass
from collections import defaultdict
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.coords import Coords
class Square:
    def __init__(self, coords: tuple[Coords, Coords]) -> None:
        self.first, self.second = sorted(coords, reverse=True)

    def area(self) -> int:
        x_diff = abs(self.first.x - self.second.x) + 1
        y_diff = abs(self.first.y - self.second.y) + 1
        return x_diff * y_diff


class Solution(BaseSolution):
    """Solutions for day 9 of 2025's Advent of Code."""
    def _parse(self: Self) -> Any:
        return [Coords(*nums) for nums in self.line_numbers]

    def part_a(self: Self) -> int:
        """Answer part a.
        """
        areas = (Square(comb).area() for comb in itertools.combinations(self.parsed, 2))
        return max(areas)

    def part_b(self: Self) -> int:
        """Answer part b."""
        wrap = [*self.line_numbers, list(self.line_numbers[0])]
        polygon = shapely.Polygon(wrap)
        shapely.prepare(polygon)

        valid = []
        for (a, b) in itertools.combinations(self.parsed, 2):
            box = shapely.multipoints([[a.x, a.y],[b.x, b.y]])
            if polygon.covers(box.envelope):
                sq = Square((a, b)).area()
                valid.append(sq)

        return max(valid)

if __name__ == "__main__":
    submit_answers(Solution, 9, 2025)
