from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import more_itertools
from collections import deque
import itertools
import numpy as np

from aoc_cqkh42.helpers.aocr import word
from scipy.optimize import minimize

class Solution(BaseSolution):
    ys = []
    xs = []
    dy = []
    dx = []

    def _parse(self: Self) -> Any:
        for x, y, dx, dy in self.line_numbers:
            self.ys += [y]
            self.dy += [dy]
            self.dx += [dx]
            self.xs += [x]
        self.ys = np.array(self.ys)
        self.dy = np.array(self.dy)
        self.xs = np.array(self.xs)
        self.dx = np.array(self.dx)


    def variance(self, steps):
        points = self.ys + (self.dy*steps)
        mean = points.mean()
        return ((points - mean) ** 2).sum()

    def part_a(self):
        a = minimize(self.variance, 1)
        step = int(a.x)
        print(step)

        xs = self.xs + (self.dx*step)
        ys = self.ys + (self.dy*step)
        xs = xs -xs.min()
        ys = ys - ys.min()

        arr = np.full(shape=(ys.max()+1, xs.max()+2), fill_value=" ")
        for x, y in zip(xs, ys):
            arr[y][x] = "#"
        chars = []
        for row in arr:
            chars.append("".join(str(i) for i in row))
        chars = "\n".join(chars)
        print(chars)
        return word(chars, true="#")



    def part_b(self):
        a = minimize(self.variance, 1)
        return int(a.x)

if __name__ == "__main__":
    submit_answers(Solution,9, 2018)
