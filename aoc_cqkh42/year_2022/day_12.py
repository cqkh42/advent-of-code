from aoc_cqkh42 import BaseSolution

from collections import defaultdict
import networkx as nx


def manhattan(from_, to):
    return abs(from_[0] - to[0]) + abs(from_[1] - to[1])


class Solution(BaseSolution):
    lowest = []

    def is_valid_edge(self, u, v):
        f = self.lines[u[0]][u[1]]
        t = self.lines[v[0]][v[1]]
        if f == 'S':
            f = 'a'
        if t == 'E':
            t = 'z'
        if ord(t) - ord(f) <= 1:
            return True
        else:
            return False

    def label_nodes(self, graph):
        sizes = defaultdict(dict)
        for row_index, row in enumerate(self.lines):
            for col_index, val in enumerate(row):
                if val == 'S':
                    self.start = (row_index, col_index)
                    self.lowest.append((row_index, col_index))
                    sizes[(row_index, col_index)]['height'] = ord('a')
                elif val == 'E':
                    self.end = (row_index, col_index)
                    sizes[(row_index, col_index)]['height'] = ord('z')
                elif val == 'a':
                    self.lowest.append((row_index, col_index))
                    sizes[(row_index, col_index)]['height'] = ord(val)
                else:
                    sizes[(row_index, col_index)]['height'] = ord(val)
        nx.set_node_attributes(graph, sizes)

    def parse_data(self):
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
            self.parsed_data, self.start, self.end
        )
        return self.answer_a

    def part_b(self):
        shortest_lengths = dict(
            nx.single_target_shortest_path_length(
                self.parsed_data, self.end, self.answer_a
            )
        )
        return min(
            shortest_lengths.get(node, float('inf')) for node in self.lowest
        )
