import itertools
from dataclasses import dataclass, asdict
from functools import cached_property

import more_itertools
import networkx
import networkx as nx
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

PARSER = parse.compile(
    r"/dev/grid/node-x{data[x]:d}-y{data[y]:d}{:s}{data[size]:d}T{:s}{data[used]:d}"
)

#todo coords
# @dataclass(frozen=True)
class Node:
    def __init__(self, data):
        cell = PARSER.search(data)
        data = cell.named['data']
        self.x = data['x']
        self.y = data['y']
        self.size = data['size']
        self.used = data['used']

    def __iter__(self):
        yield from (
            ("x", self.x),
            ('y', self.y),
            ('size', self.size),
            ('used', self.used)
        )

    @cached_property
    def available(self):
        return self.size - self.used


class Solution(BaseSolution):
    def _parse_line(self, line: str):
        try:
            return Node(line)
        except AttributeError:
            return

    def _parse(self):
        valid_cells = more_itertools.flatten(
            (node_a, node_b)
            for (node_a), (node_b) in itertools.permutations(self.parsed_lines, 2)
            if 0 < node_a.used <= node_b.available
        )

        in_scope_nodes = {(node.x, node.y): node for node in valid_cells}

        graph = networkx.grid_graph(
            (
                max(self.parsed_lines, key=lambda cell: cell.y).y + 1,
                max(self.parsed_lines, key=lambda cell: cell.x).x + 1,
            )
        )
        nx.set_node_attributes(graph, in_scope_nodes)
        not_in_name_nodes = set(graph.nodes).difference(in_scope_nodes)
        graph.remove_nodes_from(not_in_name_nodes)
        return graph

    def part_a(self):
        return len(self.parsed) - 1  # we exclude the empty node here

    def part_b(self):
        max_x = max(self.parsed, key=lambda x: x[0])[0]
        empty = more_itertools.only(
            k for k, v in self.parsed.nodes.items() if v["used"] == 0
        )
        a = networkx.shortest_path_length(self.parsed, empty, (max_x, 0))
        return a + ((max_x - 1) * 5)


if __name__ == "__main__":
    submit_answers(Solution, 22, 2016)
