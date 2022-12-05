import numpy as np
from scipy.ndimage import generic_filter

from aoc_cqkh42 import BaseSolution


def iteration(lights):
    f = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    neighbours = generic_filter(
        lights, lambda x: x.sum(), footprint=f, mode="constant", output=int
    )
    threes = neighbours == 3
    two_or_three = (neighbours == 2) | threes
    stays_on = lights & two_or_three
    turns_on = threes & ~lights
    lights = stays_on | turns_on
    return lights


class Solution(BaseSolution):
    def parse_data(self):
        rows = [list(row) for row in self.lines]
        rows = np.array(rows)
        rows = rows == "#"
        return rows

    def part_a(self, steps=100):
        light_arr = self.parsed_data.copy()
        for _ in range(steps):
            light_arr = iteration(light_arr)
        return light_arr.sum()

    def part_b(self, steps=100):
        light_arr = self.parsed_data
        light_arr[[0, 0, -1, -1], [0, -1, 0, -1]] = 1

        for _ in range(steps):
            light_arr = iteration(light_arr)
            light_arr[[0, 0, -1, -1], [0, -1, 0, -1]] = 1
        return light_arr.sum()
