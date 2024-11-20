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
    PARSER = parse.compile("{:w} {:d},{:d} through {:d},{:d}")

    def run_cycle(self, actions):
        lights = np.zeros((1000, 1000), dtype=int)
        for action, x_slice, y_slice in self.parsed_lines:
            lights[x_slice, y_slice] = actions[action](lights[x_slice, y_slice])
        return lights.sum()

    def part_a(self):
        actions =  {
            'on': lambda x: 1,
            'off': lambda x: 0,
            'toggle': lambda x: x ^ 1
        }
        return self.run_cycle(actions)

    def part_b(self):
        actions = {
            'on': lambda x: x+1,
            'off': lambda x: np.clip(x-1, a_min=0, a_max=None),
            'toggle': lambda x: x+2
        }
        return self.run_cycle(actions)

    def _parse_line(self, line: str):
        action, x_start, y_start, x_end, y_end = self.PARSER.search(line.replace('turn ', ''))
        return action, slice(x_start, x_end + 1), slice(y_start, y_end + 1)


if __name__ == "__main__":
    submit_answers(Solution, 6, 2015)
