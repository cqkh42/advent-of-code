#!/usr/bin/python3
"""Solutions for day 8 of 2025's Advent of Code.

Read the full puzzle at https://adventofcode.com/2025/day/8
"""
__all__ = ["Solution"]

import itertools
import math

import networkx as nx
from typing import Self
import re
import more_itertools
from collections import defaultdict
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

from scipy.spatial.distance import pdist
from sklearn.metrics import pairwise_distances

FUNCS = {"*": math.prod, "+": sum}

def distance(pair):
    l, r = pair
    return ((l[0] - r[0])**2) + ((l[1] - r[1])**2 )+ ((l[2] - r[2])**2)
class Solution(BaseSolution):
    """Solutions for day 8 of 2025's Advent of Code."""

    def part_a(self: Self, n=1000) -> int:
        """Answer part a.
        """
        triples = [tuple(triple) for triple in more_itertools.chunked(self.numbers, 3)]
        graph = nx.Graph()
        s = sorted(itertools.combinations(triples, 2), key=distance)
        graph.add_edges_from(s[:n])

        cycles = sorted((len(component) for component in nx.connected_components(graph)), reverse=True)
        return math.prod(cycles[:3])

    def part_b(self: Self) -> int:
        """Answer part b."""
        triples = [tuple(triple) for triple in more_itertools.chunked(self.numbers, 3)]
        graph = nx.Graph()
        graph.add_nodes_from(triples)
        s = sorted(itertools.combinations(triples, 2), key=distance)
        for a, b in s:
            graph.add_edge(a, b)
            if more_itertools.ilen(nx.connected_components(graph)) == 1:
                return a[0] * b[0]






if __name__ == "__main__":
    submit_answers(Solution, 8, 2025)
