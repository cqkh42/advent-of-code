from dataclasses import dataclass, field
import math

import numpy as np
from scipy.ndimage import generic_filter

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.helpers.graph.bfs import BFS, BFSBaseState


@dataclass(frozen=True)
class State(BFSBaseState):
    x: int
    y: int
    arr: np.array = field(compare=False)

    def is_target(self):
        return False

    def is_valid(self):
        max_x, max_y = self.arr.shape
        return self.x < max_x and self.y < max_y and self.arr[self.x, self.y] != 9 and self.x >= 0 and self.y >= 0

    def neighbours(self):
        states = [
            State(self.x - 1, self.y, self.arr),
            State(self.x + 1, self.y, self.arr),
            State(self.x, self.y - 1, self.arr),
            State(self.x, self.y + 1, self.arr)
        ]
        return [state for state in states if state.is_valid()]


class Solution(BaseSolution):
    def part_a(self):
        arr = np.array([list(i) for i in self.lines]).astype(int)
        f = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

        neighbours = generic_filter(arr, lambda x: x.min(), footprint=f,
                                    mode='constant', output=int, cval=10)
        answer = (arr[arr < neighbours] + 1).sum()

        return answer

    def part_b(self):
        arr = np.array([list(i) for i in self.lines]).astype(int)
        f = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

        neighbours = generic_filter(arr, lambda x: x.min(), footprint=f,
                                    mode='constant', output=int, cval=10)
        peaks = np.argwhere(arr < neighbours)

        a = [State(*i, arr) for i in peaks]
        a = [BFS(start) for start in a]
        for i in a:
            i.run()
        a = [len(a.visited) for a in a]
        a = sorted(a, reverse=True)
        return math.prod(a[:3])
