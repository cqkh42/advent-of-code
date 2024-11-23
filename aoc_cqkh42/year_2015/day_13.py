import itertools
from collections import defaultdict

import more_itertools
import networkx as nx
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    PARSER = parse.compile(
        r"{:w} would {:d} happiness units by sitting next to {:w}.")
    def _parse(self):
        a = defaultdict(int)
        for persons, value in self.parsed_lines:
            a[persons] += value
        graph = nx.Graph()
        for (person_a, person_b), val in a.items():
            graph.add_edge(person_a, person_b, weight=val)

        circle_routes = ([*i, i[0]] for i in itertools.permutations(graph))
        paths = [
            [
                graph.edges[start, end]["weight"]
                for start, end in more_itertools.pairwise(route)
            ]
            for route in circle_routes
        ]
        return [(sum(path), min(path)) for path in paths]

    def _parse_line(self, line: str):
        a = line.replace("lose ", "-").replace("gain ", "")
        p_1, val, p_2 = self.PARSER.search(a)
        return frozenset({p_1, p_2}), val


    def part_a(self):
        return max(self.parsed)[0]

    def part_b(self):
        return max(weight - lowest for weight, lowest in self.parsed)


if __name__ == "__main__":
    submit_answers(Solution, 13, 2015)
