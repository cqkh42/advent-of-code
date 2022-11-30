import itertools
from io import StringIO

from aoc_cqkh42 import BaseSolution

import networkx as nx
import numpy as np


def heuristic(a, b):
    a_diff = abs(a[0] - b[0])
    b_diff = abs(a[1] - b[1])
    return a_diff+b_diff

def make_big_square(start):
    pieces = [start]
    for i in range(4):
        new_piece = pieces[-1]+1
        new_piece[new_piece > 9] = 1
        pieces.append(new_piece)
    column = np.concatenate(pieces, axis=0)

    columns = [column]
    for i in range(4):
        new_column = columns[-1] + 1
        new_column[new_column > 9] = 1
        columns.append(new_column)
    big = np.concatenate(columns, axis=1)
    return big


class Solution(BaseSolution):
    def parse_data(self):
        array = []
        for line in self.lines:
            line = [int(i) for i in line]
            array.append(line)
        array = np.array(array)
        big_square = make_big_square(array)

        graph = nx.grid_2d_graph(*big_square.shape, create_using=nx.DiGraph)
        it = np.nditer(big_square, flags=['multi_index'])
        for weight in it:
            x, y = it.multi_index
            graph.add_edge((x-1, y),(x, y) , weight=weight.max())
            graph.add_edge((x+1, y),(x, y), weight=weight.max())
            graph.add_edge((x, y-1),(x, y), weight=weight.max())
            graph.add_edge((x, y+1), (x, y), weight=weight.max())
        return graph

    def part_a(self):
        target = (len(self.lines)-1, len(self.lines)-1)
        a_star = nx.shortest_paths.astar_path(self.parsed_data, (0, 0), target, heuristic=heuristic, weight='weight')
        return sum(self.parsed_data.edges[i]['weight'] for i in zip(a_star, a_star[1:]))

    def part_b(self):
        target = ((len(self.lines)*5)-1, (len(self.lines)*5)-1)
        a_star = nx.shortest_paths.astar_path(self.parsed_data, (0, 0), target,
                                              heuristic=heuristic,
                                              weight='weight')
        return sum(
            self.parsed_data.edges[i]['weight'] for i in zip(a_star, a_star[1:]))
