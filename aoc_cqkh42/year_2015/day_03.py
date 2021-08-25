import itertools
import operator

import numpy as np

from aoc_cqkh42 import BaseSolution


def _trace_path(steps):
    mapping_dict = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    changes = (mapping_dict[step] for step in steps)
    coords = itertools.accumulate(
        changes, operator.add, initial=np.array([0, 0])
    )
    return np.array(list(coords))


class Solution(BaseSolution):
    def part_a(self):
        coords = _trace_path(self.data)
        unique = np.unique(coords, axis=0)
        return len(unique)

    def part_b(self):
        santa = _trace_path(self.data[::2])
        robo = _trace_path(self.data[1::2])
        all_coords = np.concatenate((santa, robo))
        unique = np.unique(all_coords, axis=0)
        return len(unique)
