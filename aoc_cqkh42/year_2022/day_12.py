from collections import defaultdict

import more_itertools
import networkx as nx

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    lowest = []

    def is_valid_edge(self, u, v):
        f = self.lines[u[0]][u[1]]
        t = self.lines[v[0]][v[1]]
        f = 'a' if f == 'S' else f
        t = 'z' if t == 'E' else t
        return ord(t) - ord(f) <= 1

    def label_nodes(self, graph):
        sizes = defaultdict(dict)
        for row_index, row in enumerate(self.lines):
            for col_index, val in enumerate(row):
                mapped_val = val.translate({83: 97, 69: 90})
                sizes[(row_index, col_index)]['true_val'] = val
                sizes[(row_index, col_index)]['height'] = mapped_val
        nx.set_node_attributes(graph, sizes)

    @property
    def start(self):
        return more_itertools.one(
            node for node, data in self.processed.nodes(data=True) if
            data.get('true_val') == 'S')

    @property
    def end(self):
        return more_itertools.one(
            node for node, data in self.processed.nodes(data=True) if
            data.get('true_val') == 'E')

    def _process_data(self):
        graph = nx.grid_2d_graph(
            len(self.lines), len(self.lines[0]), create_using=nx.DiGraph
        )
        to_remove = [
            edge for edge in graph.edges if not self.is_valid_edge(*edge)
        ]
        for t in to_remove:
            graph.remove_edge(*t)
        self.label_nodes(graph)
        return graph

    def part_a(self):
        self.answer_a = nx.shortest_path_length(
            self.processed, self.start, self.end
        )
        return self.answer_a

    def part_b(self):
        lowest = [node for node, data in self.processed.nodes(data=True) if
                  data['height'] == 'a']
        shortest_lengths = dict(
            nx.single_target_shortest_path_length(
                self.processed, self.end, self.answer_a
            )
        )
        return min(
            shortest_lengths.get(node, float('inf')) for node in lowest
        )
