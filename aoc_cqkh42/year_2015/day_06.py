#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/6
"""
__all__ = ["Solution"]
import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 6 of 2015's Advent of Code."""

    def part_a(self):
        lights = np.zeros((1000, 1000), dtype=int)
        for action, x_slice, y_slice in self.processed:
            match action:
                case "on":
                    lights[x_slice, y_slice] = 1
                case "off":
                    lights[x_slice, y_slice] = 0
                case _:
                    lights[x_slice, y_slice] ^= 1
        return str(lights.sum())

    def part_b(self):
        lights = np.zeros((1000, 1000), dtype=int)
        for action, x_slice, y_slice in self.processed:
            match action:
                case "on":
                    lights[x_slice, y_slice] += 1
                case "toggle":
                    lights[x_slice, y_slice] += 2
                case _:
                    lights[x_slice, y_slice] -= 1
                    lights = np.clip(lights, a_min=0, a_max=None)
        return str(lights.sum())

    def _process_data(self):
        parser = parse.compile("{:w} {:d},{:d} through {:d},{:d}")
        tidied = self.input_.replace("turn ", "")
        instructions = parser.findall(tidied)
        instructions = [
            (action, slice(x_start, x_end + 1), slice(y_start, y_end + 1))
            for action, x_start, y_start, x_end, y_end in instructions
        ]
        return instructions


if __name__ == "__main__":
    submit_answers(Solution, 6, 2015)
