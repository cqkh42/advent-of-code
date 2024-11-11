from typing import Self, Any

import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        # https://www.redblobgames.com/grids/hexagons/#neighbors is
        # the gold standard
        q_map = {"ne": 1, "sw": -1, "se": 1, "nw": -1}
        r_map = {"n": -1, "s": 1, "ne": -1, "sw": 1}
        s_map = {"n": 1, "s": -1, "se": -1, "nw": 1}

        steps = [
            (s_map.get(char, 0), r_map.get(char, 0), q_map.get(char, 0))
            for char in self.input_.split(",")
        ]
        accumulated = np.cumsum(steps, axis=0)
        distances = np.absolute(accumulated).sum(axis=1) / 2
        return distances

    def part_a(self):
        return int(self.processed[-1])

    def part_b(self):
        return int(self.processed.max())


if __name__ == "__main__":
    submit_answers(Solution, 11, 2017)
