from functools import cached_property
from typing import Self, Any

import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Region:
    def __init__(self, nodes):
        self.nodes = nodes

    @cached_property
    def perimeter(self):
        total = 0
        for x, y in self:
            if (x + 1, y) not in self:
                total += 1
            if (x - 1, y) not in self:
                total += 1
            if (x, y + 1) not in self:
                total += 1
            if (x, y - 1) not in self:
                total += 1
        return total

    @cached_property
    def sides(self):
        potential_lefts = [(x, y) for (x,y) in self if (x-1, y) not in self]
        lefts = [(x, y+1) not in potential_lefts for x, y in potential_lefts]

        potential_rights = [(x, y) for (x,y) in self if (x+1, y) not in self]
        rights = [(x, y + 1) not in potential_rights for x, y in potential_rights]

        potential_tops = [(x, y) for (x,y) in self if (x, y+1) not in self]
        tops = [(x+1, y) not in potential_tops for x, y in potential_tops]

        potential_bottoms = [(x, y) for (x,y) in self if (x, y-1) not in self]
        bottoms = [(x + 1, y) not in potential_bottoms for x, y in potential_bottoms]

        return sum(tops) + sum(bottoms) + sum(rights) + sum(lefts)

    def __repr__(self):
        return f'Region({self.nodes})'


    def __iter__(self):
        yield from self.nodes

    def __len__(self):
        return len(self.nodes)


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        G = nx.grid_2d_graph(self.num_lines, len(self.lines[0]))
        for left, right in G.edges:
            if self.lines[left[0]][left[1]] != self.lines[right[0]][right[1]]:
                G.remove_edge(left, right)
        return [Region(nodes) for nodes in nx.connected_components(G)]

    def part_a(self):
        return sum(region.perimeter * len(region) for region in self.parsed)

    def part_b(self):
        return sum(region.sides * len(region) for region in self.parsed)


if __name__ == "__main__":
    submit_answers(Solution,12, 2024)
