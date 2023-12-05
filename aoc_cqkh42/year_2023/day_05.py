#!/usr/bin/python3
"""Solutions for day 4 of 2023's Advent of Code.

Read the full puzzle at https://adventofcode.com/2023/day/4
"""
__all__ = ["Solution"]

import functools
from typing import Self

import more_itertools
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution



def do_stage(inputs, mapping):
    mapping = [tuple(int(i) for i in row.split()) for row in mapping]
    mapping = [tuple((*i, i[1]+i[2]-1)) for i in mapping]
    new_inputs = []

    for num in inputs:
        k = (left + num - right for left, right, size, window in mapping if
             right <= num <= window)
        new_inputs.append(more_itertools.first(k, num))
    return new_inputs


NUM_FINDER = parse.compile(r'{num:d}')

def do_all(seeds, mappings):
    for mapping in mappings:
        mapping = mapping[1:]
        seeds = do_stage(seeds, mapping)
    return seeds


class Solution(BaseSolution):
    """Solutions for day 4 of 2023's Advent of Code."""

    def _process_data(self: Self) -> tuple[int, ...]:
        return None

    def part_a(self: Self) -> int:
        seeds = [i['num'] for i in NUM_FINDER.findall(self.lines[0])]
        mappings = more_itertools.split_at(self.lines[2:], lambda x: x == '')
        seeds = do_all(seeds, mappings)
        return min(seeds)

    def part_b(self: Self) -> int:
        seeds = [i['num'] for i in NUM_FINDER.findall(self.lines[0])]
        seeds = more_itertools.chunked(seeds, 2)
        mappings = more_itertools.split_at(self.lines[2:], lambda x: x == '')

        for a,b in seeds:
            k = do_all([i for i in range(a, a+b)], mappings)
            print(min(k))
        # print(list(seeds))



if __name__ == "__main__":
    submit_answers(Solution, 4, 2023)
