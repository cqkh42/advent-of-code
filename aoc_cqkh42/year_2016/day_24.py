from collections import defaultdict
import itertools
import more_itertools
from typing import Self

from aoc_cqkh42.helpers.base_solution import BaseSolution

import numpy as np
import networkx as nx

def calc_distance(path, distances):
    distance =  sum(distances[x][y] for x, y in more_itertools.pairwise(path))
    return distance


class Solution(BaseSolution):
    def parse_data(self):
        a = [list(line) for line in self.input_.split()]
        a = np.array(a)

        return self.input_
    def part_a(self: Self) -> int:
        a = [list(line) for line in self.input_.split()]
        # print(a)
        a = np.array(a)
        # print(a.shape)
        locations = {}
        x = a.shape
        g = nx.grid_graph([x[1],x[0]])
        hashes = np.transpose((a == '#').nonzero())
        hashes = [tuple(i) for i in hashes.tolist()]
        # print(np.where(a == '#'))
        # print()
        # can use a complete graph here
        g.remove_nodes_from(hashes)

        for num in range(10):
            if str(num) in a:
                # print(num)
                location = tuple(np.transpose((a == f'{num}').nonzero())[0].tolist())
                locations[num] = location
        # print(locations)

        paths = defaultdict(dict)
        for a, b in itertools.combinations(locations, 2):
            distance = nx.shortest_path_length(g, locations[a], locations[b])
            paths[a][b] = distance
            paths[b][a] = distance

        possible_paths = itertools.permutations(locations, len(locations))
        return min(calc_distance(path, paths) for path in possible_paths)


    def part_b(self: Self) -> str | int:
        a = [list(line) for line in self.input_.split()]
        a = np.array(a)
        locations = {}
        x = a.shape
        g = nx.grid_graph([x[1], x[0]])
        hashes = np.transpose((a == '#').nonzero())
        hashes = [tuple(i) for i in hashes.tolist()]
        g.remove_nodes_from(hashes)

        for num in range(10):
            if str(num) in a:
                location = tuple(
                    np.transpose((a == f'{num}').nonzero())[0].tolist())
                locations[num] = location

        paths = defaultdict(dict)
        non_zero_locations = {k: v for k, v in locations.items() if k != 0}
        for a, b in itertools.combinations(locations, 2):
            distance = nx.shortest_path_length(g, locations[a], locations[b])
            paths[a][b] = distance
            paths[b][a] = distance

        possible_paths = itertools.permutations(non_zero_locations, len(non_zero_locations))
        possible_paths = [[0, *path, 0] for path in possible_paths]
        return min(calc_distance(path, paths) for path in possible_paths)