from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
import more_itertools
from collections import deque
import itertools
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

from aoc_cqkh42.helpers.aocr import word
from scipy.optimize import minimize

class Solution(BaseSolution):
    def _parse(self):
        x = np.arange(1, 301) + 10
        y = np.arange(1, 301).reshape((-1, 1))
        power = (x * y) + self.number
        power *= x
        power %= 1000
        power //= 100
        power -= 5
        return power

    def _window(self, size=3):
        windows= sliding_window_view(self.parsed, (size,size))
        return windows.sum(axis=(2,3))


    def part_a(self, grid_size=300):
        argmax = self._window().argmax()
        y = (argmax // 298) + 1
        x = (argmax % 298) + 1
        return f"{x},{y}"

    def part_b(self):
        windows = {size: self._window(size) for size in range(1, 301)}
        max_window_size = max(windows, key=lambda key: windows[key].max())
        window = windows[max_window_size]
        argmax = window.argmax()
        y = (argmax // (301-max_window_size)) + 1
        x = (argmax % (301-max_window_size)) + 1
        return f"{x},{y},{max_window_size}"

if __name__ == "__main__":
    submit_answers(Solution,9, 2018)
