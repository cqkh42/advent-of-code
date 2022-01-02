import numpy as np
from scipy.ndimage import generic_filter

from aoc_cqkh42 import BaseSolution


def step(arr):
    # add 1 to everything
    # increase all neighbours
    # burn all 10s we just used (not new 10s)
    out = arr + 1

    f = [[1, 1,1], [1, 0, 1], [1, 1, 1]]
    while True:
        neighbours = generic_filter(arr, lambda x: (x == 10).sum(), footprint=f,
                                mode='constant', output=int, cval=0)
        new_out = out + neighbours
        new_out[(out+neighbours > 10) & (neighbours != 0)] = 10
        print()
        print(new_out)
        if (new_out.clip(max=10) == out.clip(max=10)).all():
            new_out[new_out >= 10] = 0
            print()
            print(new_out)
            return new_out
        out = new_out


class Solution(BaseSolution):
    def part_a(self):
        total = 0
        a = [list(line) for line in self.lines]
        arr = np.array([list(line) for line in self.lines]).astype(int)
        for i in range(100):
            arr = step(arr)
            total += (arr == 0).sum()
        return total


    def part_b(self):
        ...
