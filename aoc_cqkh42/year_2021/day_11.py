import itertools

import numpy as np
from scipy.ndimage import generic_filter

from aoc_cqkh42.helpers.base_solution import BaseSolution


def step(consortium):
    flashed = np.zeros_like(consortium)
    consortium += 1
    will_flash = consortium > 9
    while will_flash.any():
        f = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        neighbours = generic_filter(will_flash, sum,
                                    footprint=f,
                                    mode='constant', output=int,
                                    cval=0)
        consortium += neighbours
        flashed = np.logical_or(flashed, will_flash)
        will_flash = np.logical_and(consortium > 9, flashed != 1)
    consortium[consortium > 9] = 0
    return consortium


class Solution(BaseSolution):
    flashes = 0

    def _process_data(self):
        return np.array([list(line) for line in self.lines]).astype(int)

    def step(self):
        flashed = np.zeros_like(self.parsed_data)
        self.parsed_data += 1
        will_flash = self.parsed_data > 9
        while will_flash.any():
            f = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
            neighbours = generic_filter(will_flash, sum,
                                        footprint=f,
                                        mode='constant', output=int,
                                        cval=0)
            self.parsed_data += neighbours
            flashed = np.logical_or(flashed, will_flash)
            will_flash = np.logical_and(self.parsed_data > 9, flashed != 1)
        self.parsed_data[self.parsed_data > 9] = 0
        self.flashes += flashed.sum()
        return self.parsed_data

    def part_a(self):
        for _ in range(100):
            self.step()
        return self.flashes

    def part_b(self):
        self.parsed_data = self._process_data()
        for step in itertools.count(1):
            self.step()
            if self.parsed_data.sum() == 0:
                return step

