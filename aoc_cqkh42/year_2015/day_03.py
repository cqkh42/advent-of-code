import itertools

import numpy as np

from aoc_cqkh42 import BaseSolution

def _trace_path(steps):
    mapping_dict = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    changes = (mapping_dict[step] for step in steps)
    a = itertools.accumulate(changes, np.add, initial=np.array([0, 0]))
    b = {tuple(i.tolist()) for i in a}
    return b


class Solution(BaseSolution):
    def part_a(self):
        return len(_trace_path(self.data))

    def part_b(self):
        santa = _trace_path(self.data[::2])
        robo = _trace_path(self.data[1::2])
        visited = {*santa, *robo}
        return len(visited)
