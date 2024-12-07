import itertools
from typing import Self

import more_itertools
import networkx as nx

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
    values = None
    def _parse(self: Self) -> nx.Graph:
        nodes = [tuple(nums) for nums in more_itertools.chunked(self.numbers, 2)]
        g = nx.Graph()
        for node in nodes:
            g.add_node(node)
        for a, b in itertools.combinations(nodes, 2):
            if set(a).intersection(b):
                g.add_edge(a, b)

        self.values = {
            node: sum(node) for node in nodes
        }
        return g

    def greedy(self, visited):
        current_node = visited[-1]
        if len(visited) == 1:
            # this is first
            potential_options = [node for node in self.parsed if set(node).intersection(current_node) and node not in visited]
        elif visited[-1][0] in visited[-2]:
            free_edge = visited[-1][1]
            potential_options = [node for node in self.parsed if node not in visited and free_edge in node]
        else:
            free_edge = visited[-1][0]
            potential_options = [node for node in self.parsed if
                                 node not in visited and free_edge in node]
        if not potential_options:
            return visited
        else:
            m = max(potential_options, key=sum)
            return self.greedy(visited +[m])


    def part_a(self):
        starts = [node for node in self.parsed if 0 in node]
        # print(starts, all_nodes)
        for start in starts:
            a = [(node, nx.has_path(self.parsed, start, node)) for node in self.parsed]
            paths = [list(nx.all_simple_paths(self.parsed, start, node)) for node, path in a if path]
            print(a, paths)


    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,24, 2017)
