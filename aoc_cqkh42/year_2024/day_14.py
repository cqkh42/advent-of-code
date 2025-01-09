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

        a = np.repeat(velocities[:, :, np.newaxis], N_SECS, axis=2).cumsum(
            axis=2) + np.repeat(starts[:, :, np.newaxis], N_SECS, axis=2)
        mods = np.array([[
            [101] * N_SECS,
            [103] * N_SECS
        ]]*500)
        a %= mods

        tl = np.logical_and(a[:, 0, :] < 50, a[:, 1, :] < 51).sum(axis=0)
        bl = np.logical_and(a[:, 0, :] < 50, a[:, 1, :] > 51).sum(axis=0)
        tr = np.logical_and(a[:, 0, :] > 50, a[:, 1, :] < 51).sum(axis=0)
        br = np.logical_and(a[:, 0, :] > 50, a[:, 1, :] > 51).sum(axis=0)

        return tl * tr * br * bl
    def part_a(self):
        return self.parsed[99]

    def part_b(self):
        #uses a hack I found that the christmas tree occurs when the safety factor is minimised
        return np.argmin(self.parsed)+1

if __name__ == "__main__":
    submit_answers(Solution,14, 2024)
