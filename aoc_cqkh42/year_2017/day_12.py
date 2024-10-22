from typing import Self, Any

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

import more_itertools
import networkx as nx

class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        g = nx.Graph()

        for line in self.lines:
            left, right = line.split(' <-> ')
            right = right.split(', ')
            for r in right:
                g.add_edge(left, r)
        return g

    def part_a(self):
        return sum(
            nx.has_path(self.processed, node, '0')
            for node in self.processed
        )

    def part_b(self):
        return more_itertools.ilen(nx.connected_components(self.processed))


if __name__ == "__main__":
    submit_answers(Solution, 12, 2017)