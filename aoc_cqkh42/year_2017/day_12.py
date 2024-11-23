from typing import Self, Any

import more_itertools
import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        g = nx.Graph()

        for left, right in self.parsed_lines:
            for r in right:
                g.add_edge(left, r)
        return g

    def _parse_line(self, line: str):
        left, right = line.split(" <-> ")
        right = right.split(', ')
        return left, right

    def part_a(self):
        return sum(nx.has_path(self.parsed, node, "0") for node in self.parsed)

    def part_b(self):
        return more_itertools.ilen(nx.connected_components(self.parsed))


if __name__ == "__main__":
    submit_answers(Solution, 12, 2017)
