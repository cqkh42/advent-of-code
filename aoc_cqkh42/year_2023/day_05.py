#!/usr/bin/python3
"""Solutions for day 5 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/5
"""
__all__ = ["Solution"]

import functools
import itertools
from typing import Self

import more_itertools
import parse
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution



NUM_FINDER = parse.compile(r'{num:d}')


def do(seeds, mappings):
    for mapping in mappings:
        modified = np.zeros_like(seeds)
        for destination, source, range in mapping:
            about_to_move = (seeds >= source) & (seeds <= source + range) & (
                        modified == 0)
            seeds[about_to_move] = seeds[about_to_move] - source + destination
            modified = modified | about_to_move
    return seeds

def do_2(seeds, mappings):
    for mapping in mappings:
        modified = np.zeros_like(seeds)
        for source, destination, range in mapping:
            about_to_move = (seeds >= source) & (seeds <= source + range) & (
                        modified == 0)
            seeds[about_to_move] = seeds[about_to_move] - source + destination
            modified = modified | about_to_move
    return seeds


class Solution(BaseSolution):
    """Solutions for day 5 of 2023's Advent of Code."""
    def mappings(self):
        mappings = more_itertools.split_at(self.lines[2:], lambda x: x == '')
        for mapping in mappings:
            yield [[int(i) for i in row.split()] for row in mapping[1:]]

    def part_a(self: Self) -> int:
        seeds = np.array([i['num'] for i in NUM_FINDER.findall(self.lines[0])])
        return min(do(seeds, self.mappings()))

    def seed_ranges(self):
        end_seeds = np.array(
            [i['num'] for i in NUM_FINDER.findall(self.lines[0])])
        end_ranges = more_itertools.chunked(end_seeds, 2)
        end_ranges = [range(a, a + b) for a, b in end_ranges]
        return end_ranges

    def part_b(self: Self) -> int:
        end_seeds = self.seed_ranges()
        mappings = [i for i in more_itertools.always_reversible(self.mappings())]

        for i in itertools.count(0, 50):
            locations = np.arange(i, i+50)
            k = do_2(locations, mappings)
            print(k, len(k))
            print(end_seeds)
            raise
        first = mappings[0]
        first = [range(i[1], i[1]+i[2]) for i in first]
        print(first)
        print(end_seeds)

if __name__ == "__main__":
    submit_answers(Solution, 5, 2023)
