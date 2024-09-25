from functools import cached_property
import itertools

import more_itertools
import networkx
import networkx as nx
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

PARSER = parse.compile(
    r'/dev/grid/node-x{data[x]:d}-y{data[y]:d}{:s}{data[size]:d}T{:s}{data[used]:d}'
)


class Solution(BaseSolution):
    def _process_data(self):
        rows = PARSER.findall(self.input_)
        cells = {
            (cell['x'], cell['y']): {'size': cell['size'], 'used': cell['used']}
            for cell in [(row.named['data']) for row in rows]
        }

        possible_combinations = [
            (node_a_k, node_b_k)
            for (node_a_k, node_a_v), (node_b_k, node_b_v) in itertools.permutations(cells.items(), 2) if
            (node_a_v['used'] and node_a_v['used'] <= node_b_v['size'] - node_b_v['used'])
        ]

        in_game_nodes = set(more_itertools.flatten(possible_combinations))
        x_s = max(i[0] + 1 for i in cells)
        y_s = max(i[1] + 1 for i in cells)
        graph = networkx.grid_graph((y_s, x_s))
        nx.set_node_attributes(graph, cells)
        not_in_name_nodes = set(graph.nodes).difference(in_game_nodes)
        graph.remove_nodes_from(not_in_name_nodes)
        return graph

    def part_a(self):
        return len(self.processed) -1

    def part_b(self):
        max_x = max(self.processed, key=lambda x: x[0])[0]
        empty = more_itertools.only(k for k, v in self.processed.nodes.items() if v['used'] == 0)
        a = networkx.shortest_path_length(self.processed, empty, (max_x, 0))
        part_a = a
        part_b = (max_x-1)*5
        return part_a + part_b


if __name__ == "__main__":
    submit_answers(Solution, 22, 2016)
