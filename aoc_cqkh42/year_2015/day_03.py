import itertools

from aoc_cqkh42 import BaseSolution

def _trace_path(steps):
    mapping_dict = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    x, y = zip(*(mapping_dict[step] for step in steps))
    x = itertools.accumulate(x)
    y = itertools.accumulate(y)
    visited = set(zip(x, y))
    visited.add((0, 0))
    return visited


class Solution(BaseSolution):
    def part_a(self):
        return len(_trace_path(self.data))

    def part_b(self):
        santa = _trace_path(self.data[::2])
        robo = _trace_path(self.data[1::2])
        visited = {*santa, *robo}
        return len(visited)
