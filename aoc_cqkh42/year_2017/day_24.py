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

    def part_a(self):
        connected_nodes = [sum(node) for node in self.parsed if len(list(self.parsed.neighbors(node)))]
        highest_value_connected_node = max(connected_nodes)

        for node in [node for node in self.parsed if not len(list(self.parsed.neighbors(node)))]:
            if sum(node) <= highest_value_connected_node:
                self.parsed.remove_node(node)

        for node in list(self.parsed):
            neighbours = list(self.parsed.neighbors(node))
            if len(neighbours) == 1:
                neighbour = more_itertools.first(neighbours)
                self.values[neighbour] += self.values[node]
                # nx.set_node_attributes(self.processed, {node: {'value': }})
                # self.parsed[neighbour]['value'] += values[node]
                self.parsed.remove_node(node)

        sinks = []
        for node in list(self.parsed):
            neighbours = list(self.parsed.neighbors(node))
            neighbour_values = {a for i in neighbours for a in i}
            for value in node:
                if value not in neighbour_values:
                    sinks.append(node)
                    continue
        print(sinks)
        for sink in sinks:
            neighbours = list(self.parsed.neighbors(sink))
            for neighbour in neighbours:
                self.values[neighbour] += self.values[sink]
            self.parsed.remove_node(sink)



        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.parsed)
        nx.draw_networkx_labels(self.parsed, pos)
        nx.draw_networkx_nodes(self.parsed, pos=pos)
        nx.draw_networkx_edges(self.parsed, pos)
        plt.show()
        return

    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,24, 2017)
