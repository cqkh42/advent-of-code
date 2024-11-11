import itertools

import networkx as nx
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile(r"{:w} would {:d} happiness units by sitting next to {:w}.")


class Solution(BaseSolution):
    def _process_data(self):
        graph = nx.Graph()
        data = self.input_.replace("lose ", "-").replace("gain ", "")
        matches = PARSER.findall(data)
        for a, change, b in matches:
            if graph.has_edge(a, b):
                graph.edges[a, b]["weight"] += change
            else:
                graph.add_edge(a, b, weight=change)

        perms = ([*i, i[0]] for i in itertools.permutations(graph))
        weights = (
            [graph.edges[u, v]["weight"] for u, v in zip(path, path[1:])]
            for path in perms
        )
        return [(sum(weight), min(weight)) for weight in weights]

    def part_a(self):
        return max(self.processed)[0]

    def part_b(self):
        return max(weight - lowest for weight, lowest in self.processed)


if __name__ == "__main__":
    submit_answers(Solution, 13, 2015)
