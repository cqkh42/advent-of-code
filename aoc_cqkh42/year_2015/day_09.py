import itertools

import parse
import networkx as nx

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile(r'{:w} to {:w} = {:d}')

    def parse_data(self):
        graph = nx.Graph(
            (a, b, {'weight': c}) for a, b, c in self.parser.findall(self.data)
        )
        distances = {
            sum(graph.edges[start, end]['weight'] for start, end in
                zip(route, route[1:]))
            for route in itertools.permutations(graph)
        }
        return distances

    def part_a(self):
        return min(self.parsed_data)

    def part_b(self):
        return max(self.parsed_data)
