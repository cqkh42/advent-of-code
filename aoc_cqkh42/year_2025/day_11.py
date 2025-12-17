#!/usr/bin/python3
"""Solutions for day 11 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/1
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

from pulp import PULP_CBC_CMD

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.coords import Coords
import pulp
import string
class Solution(BaseSolution):
    """Solutions for day 11 of 2025's Advent of Code."""
    LINE_REGEX = re.compile(r"\w{3}")

    def _parse_line(self, line: str):
        return self.LINE_REGEX.findall(line)

    def _parse(self: Self) -> Any:
        graph = nx.DiGraph()
        dic = {input_: set(outputs) for input_, outputs in self.parsed_lines}

        for input_, *outputs in self.parsed_lines:
            for output in outputs:
                graph.add_edge(input_, output)
        return graph
    def part_a(self: Self) -> int:
        """Answer part a.
        """
        paths = nx.all_simple_paths(self.parsed, source="you", target="out")
        return more_itertools.ilen(paths)

    def part_b(self: Self) -> int:
        """Answer part b."""
        for node in self.parsed:
            if self.parsed.in_degree(node) == self.parsed.out_degree(node):

        paths = nx.all_simple_paths(self.parsed, source="svr", target="out")
        return sum("dac" in path and "fft" in path for path in paths)
        # svr to all nodes is fine
        print(self.parsed)

        for node in list(self.parsed):
            fft = nx.has_path(self.parsed, "fft", node) or nx.has_path(self.parsed, node, "fft")
            dac = fft = nx.has_path(self.parsed, "dac", node) or nx.has_path(self.parsed, node, "dac")
            out = nx.has_path(self.parsed, node, "out")
            if not all([fft, dac, out]):
                self.parsed.remove_node(node)
        svr_dac = more_itertools.ilen(nx.all_simple_paths(self.parsed, source="svr", target="out"))
        # dac_fft = more_itertools.ilen(nx.all_simple_paths(self.parsed, source="dac", target="fft"))
        # fft_out = more_itertools.ilen(nx.all_simple_paths(self.parsed, source="fft", target="out"))
        #
        # svr_fft = more_itertools.ilen(nx.all_simple_paths(self.parsed, source="svr", target="fft"))
        # fft_dac = more_itertools.ilen(nx.all_simple_paths(self.parsed, source="fft", target="dac"))
        # dac_out = more_itertools.ilen(nx.all_simple_paths(self.parsed, source="dac", target="out"))
        return

if __name__ == "__main__":
    submit_answers(Solution, 11, 2025)
