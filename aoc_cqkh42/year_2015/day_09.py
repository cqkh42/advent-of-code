#!/usr/bin/python3
"""Solutions for day 1 of 2015's Advent of Code.

Read the full puzzle at https://adventofcode.com/2015/day/9
"""
__all__ = ["Solution"]
import itertools

import more_itertools
import parse
from networkx import Graph

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    """Solutions for day 9 of 2015's Advent of Code."""

    parser = parse.compile(r"{:w} to {:w} = {:d}")

    def _process_data(self):
        graph = Graph(
            (a, b, {"weight": c}) for a, b, c in self.parser.findall(self.input_)
        )
        distances = {
            sum(
                graph.edges[start, end]["weight"]
                for start, end in more_itertools.pairwise(route)
            )
            for route in itertools.permutations(graph)
        }
        return distances

    def part_a(self):
        return min(self.processed)

    def part_b(self):
        return max(self.processed)


if __name__ == "__main__":
    submit_answers(Solution, 9, 2015)
