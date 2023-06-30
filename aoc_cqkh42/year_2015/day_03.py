import numpy as np

from aoc_cqkh42.helpers.base_solution import BaseSolution


def _unique_coords(steps) -> np.array:
    coords = np.cumsum(steps, axis=0)
    return np.unique(coords, axis=0)


class Solution(BaseSolution):
    def _process_data(self) -> np.array:
        mapping_dict = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}
        changes = np.array(
            [[0, 0], *(mapping_dict[step] for step in self.input_)]
        )
        return changes

    def part_a(self) -> int:
        return len(_unique_coords(self.processed))

    def part_b(self) -> int:
        santa = _unique_coords(self.processed[::2])
        robot = _unique_coords(self.processed[1::2])
        all_coords = np.concatenate((santa, robot))
        unique = np.unique(all_coords, axis=0)
        return len(unique)
