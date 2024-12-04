import itertools
from typing import Self, Any

import more_itertools
import networkx as nx
from networkx.algorithms.simple_paths import all_simple_paths

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def is_valid(path):
    return (
            all(
                (y[0] in x and y[1] in z) or (y[1] in x and y[0] in z) for x, y, z in more_itertools.triplewise(path)
            )
            and more_itertools.all_unique(path)
    )

class Solution(BaseSolution):
    def _parse(self: Self) -> nx.Graph:
        nodes = [tuple(nums) for nums in more_itertools.chunked(self.numbers, 2)]
        g = nx.Graph()
        g.add_nodes_from(nodes)
        for a, b in itertools.combinations(nodes, 2):
            if set(a).intersection(b):
                g.add_edge(a, b)
        return g

    def add_node(self, paths):
        for *path, end in paths:
            options = self.parsed.neighbors(end)
            for option in options:
                new_path = tuple([*path, end, option])
                if is_valid(new_path):
                    yield new_path



    def part_a(self):
        for node in self.parsed:
            print(node, len(list(self.parsed.neighbors(node))))
        return
        potential_paths = []
        paths = [tuple([node]) for node in self.parsed.nodes]
        potential_paths.extend(paths)
        while paths:
            paths = list(self.add_node(paths))
            potential_paths.extend(paths)
            print(len(paths), paths[0])
        print(potential_paths)

    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,24, 2017)
