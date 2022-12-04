import numpy as np

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self) -> np.array:
        mapping_dict = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
        changes = np.array([[0, 0], *(mapping_dict[step] for step in self.data)])
        return changes

    def part_a(self) -> int:
        coords = np.cumsum(self.parsed_data, axis=0)
        unique = np.unique(coords, axis=0)
        return len(unique)

    def part_b(self) -> int:
        santa = np.cumsum(self.parsed_data[::2], axis=0)
        robo = np.cumsum(self.parsed_data[1::2], axis=0)
        all_coords = np.concatenate((santa, robo))
        unique = np.unique(all_coords, axis=0)
        return len(unique)
