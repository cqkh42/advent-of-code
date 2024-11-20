import itertools
from collections import defaultdict
from string import ascii_uppercase
from typing import Self, Any

import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        g = nx.Graph()

        chars = defaultdict(str)
        self.chars = chars
        for y_index, row in enumerate(self.lines):
            for x_index, char in enumerate(row):
                if char != " ":
                    chars[(y_index, x_index)] = char
        valid_verticals = "|+" + ascii_uppercase
        valid_horizontals = "-+" + ascii_uppercase

        a = [(k, v) for k, v in chars.items()]

        for (y, x), char in a:
            if char in valid_verticals and chars[(y + 1, x)] in valid_verticals:
                g.add_edge((y, x), (y + 1, x), weight=1)
            elif (
                char in valid_verticals
                and chars[y + 2, x] in valid_verticals
                and chars[y + 1, x] == "-"
            ):
                g.add_edge((y, x), (y + 2, x), weight=2)
            if char in valid_horizontals and chars[y, x + 1] in valid_horizontals:
                g.add_edge((y, x), (y, x + 1), weight=1)
            elif (
                char in valid_horizontals
                and chars[y, x + 2] in valid_horizontals
                and chars[y, x + 1] == "|"
            ):
                g.add_edge((y, x), (y, x + 2), weight=2)

        x = self.lines[0].index("|")
        paths = nx.single_source_shortest_path(g, (0, x))
        longest = max(paths.values(), key=len)
        self.graph = g
        return longest

    def part_a(self):
        return "".join(self.chars[i] for i in self.parsed if self.chars[i].isalpha())

    def part_b(self):
        edge_dict = {}
        for a, b, c in self.graph.edges(data=True):
            edge_dict[(a, b)] = c["weight"]
            edge_dict[(b, a)] = c["weight"]
        distance = 0
        for a, b in itertools.pairwise(self.parsed):
            distance += edge_dict[(a, b)]
        return distance


if __name__ == "__main__":
    submit_answers(Solution, 19, 2017)
