from typing import Self, Any

import networkx as nx

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def is_wall(self, x, y):
        calc = (
                x ** 2
                + 3 * x
                + 2 * x * y
                + y
                + y ** 2
                + int(self.input_)
        )
        ones = bin(calc).count("1")
        return ones % 2

    def _parse(self: Self) -> Any:
        G = nx.grid_2d_graph(50, 50)
        i = [node for node in G if self.is_wall(*node)]
        G.remove_nodes_from(i)
        return G


    def part_a(self, target=(31,39)):
        return nx.shortest_path_length(self.parsed, (1,1), target)

    def part_b(self):
        a = nx.shortest_path_length(self.parsed, source=(1,1))
        return sum(x <= 50 for x in a.values())
