import itertools
from typing import Self, Any

import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        N_SECS = 10_000
        velocities = np.array([[c,d] for a,b,c,d in self.line_numbers])
        starts = np.array([[a,b] for a, b,c,d in self.line_numbers])
        # print(starts)
        seconds = np.array([range(N_SECS) for _ in range(self.num_lines)])

        x_locations = (velocities[:, 0].reshape(-1, 1) * seconds) + np.stack(
            [starts[:, 0]] * N_SECS, axis=1)
        x_locations %= 101

        y_locations = (velocities[:, 1].reshape(-1, 1) * seconds) + np.stack(
            [starts[:, 1]] * N_SECS, axis=1)
        y_locations %= 103

        tl = np.logical_and(x_locations < 50, y_locations < 51).sum(axis=0)
        bl = np.logical_and(x_locations < 50, y_locations > 51).sum(axis=0)
        tr = np.logical_and(x_locations > 50, y_locations < 51).sum(axis=0)
        br = np.logical_and(x_locations > 50, y_locations > 51).sum(axis=0)

        return tl * tr * br * bl
    def part_a(self):
        return self.parsed[100]

    def part_b(self):
        #uses a hack I found that the christmas tree occurs when the safety factor is minimised
        return np.argmin(self.parsed)

if __name__ == "__main__":
    submit_answers(Solution,14, 2024)
