import numpy as np
from scipy.ndimage import generic_filter

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        rows = [list(row) for row in self.data.split('\n')]
        rows = np.array(rows)
        rows = rows == '#'
        return rows


    def part_a(self):
        light_arr = self.parsed_data.copy()
        f = [[1,1,1], [1,0,1], [1,1,1]]

        for _ in range(100):
            neighbours = generic_filter(light_arr, lambda x: x.sum(), footprint=f, mode='constant', output=int)
            off = np.logical_not(light_arr)
            twos = neighbours == 2
            threes = neighbours == 3
            two_or_three = np.logical_or(twos, threes)
            on_and_on = np.logical_and(light_arr, two_or_three)
            off_and_on = threes & off
            light_arr = np.logical_or(on_and_on, off_and_on)
        return light_arr.sum()

    def part_b(self):
        light_arr = self.parsed_data
        light_arr[0, 0] = 1
        light_arr[0, -1] = 1
        light_arr[-1, 0] = 1
        light_arr[-1, -1] = 1

        for _ in range(100):
            # print(light_arr.sum())
            # print(light_arr)
            neighbours = generic_filter(light_arr, lambda x: x.sum(), footprint=[[1,1,1], [1,0,1], [1,1,1]], mode='constant', output=int)

            two_or_three = np.logical_or(neighbours == 2, neighbours == 3)
            on_and_on = light_arr & two_or_three
            off_and_on = np.logical_and(np.logical_not(light_arr), neighbours == 3)
            light_arr = np.logical_or(on_and_on, off_and_on).astype(int)
            light_arr[0,0] = 1
            light_arr[0,-1] = 1
            light_arr[-1, 0] = 1
            light_arr [-1, -1] = 1
            # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
            # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
        return light_arr.sum()
