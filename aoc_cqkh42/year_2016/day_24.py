import itertools
from collections import defaultdict
from typing import Self, Any

import more_itertools
import networkx as nx
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def calc_distance(path, distances):
    distance = sum(distances[x][y] for x, y in more_itertools.pairwise(path))
    return distance


class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        a = np.array([list(line) for line in self.input_.split()])

        x = a.shape
        g = nx.grid_graph([x[1], x[0]])
        hashes = np.transpose((a == "#").nonzero())
        hashes = [tuple(i) for i in hashes.tolist()]
        g.remove_nodes_from(hashes)

        self.locations = [None for _ in range(10)]
        for num in range(10):
            if str(num) in a:
                # print(num)
                location = tuple(np.transpose((a == f"{num}").nonzero())[0].tolist())
                self.locations[num] = location
        self.locations = [i for i in self.locations if i is not None]

        self.paths = defaultdict(dict)
        for a, b in itertools.combinations(range(len(self.locations)), 2):
            distance = nx.shortest_path_length(g, self.locations[a], self.locations[b])
            self.paths[a][b] = distance
            self.paths[b][a] = distance
        return np.array(a)

    def part_a(self: Self) -> int:
        possible_paths = itertools.permutations(
            range(len(self.locations)), len(self.locations)
        )
        return min(calc_distance(path, self.paths) for path in possible_paths)

    def part_b(self: Self) -> str | int:
        non_zero_locations = self.locations[1:]
        possible_paths = itertools.permutations(
            range(1, len(self.locations)), len(non_zero_locations)
        )
        possible_paths = [[0, *path, 0] for path in possible_paths]
        return min(calc_distance(path, self.paths) for path in possible_paths)


if __name__ == "__main__":
    submit_answers(Solution, 24, 2016)
