import itertools

import more_itertools
import parse
from networkx import Graph

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile(r"{:w} to {:w} = {:d}")

    def _process_data(self):
        graph = Graph(
            (a, b, {"weight": c}) for a, b, c in
            self.parser.findall(self.input_)
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
