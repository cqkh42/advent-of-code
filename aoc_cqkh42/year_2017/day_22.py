import itertools
from collections import defaultdict
from string import ascii_uppercase
from typing import Self, Any

import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    direction = 'N'
    current = (0, 0)
    total = 0

    def _parse(self: Self) -> Any:
        d = defaultdict(bool)
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                if value == '#':
                    d[(x_index, y_index)] = True
        x = (len(self.lines) - 1) // 2
        self.current = (x,x)
        return d

    def turn(self, change):
        v = ['N', 'E', 'S', 'W']
        current = v.index(self.direction)
        new = current + change
        self.direction = v[new % len(v)]

    def move(self):
        x, y = self.current
        if self.direction == 'N':
            self.current = x, y-1
        elif self.direction == 'E':
            self.current = x+1, y
        elif self.direction == 'S':
            self.current = x, y+1
        elif self.direction == 'W':
            self.current = x-1, y

    def __getitem__(self, item):
        return self.parsed[item]

    def __setitem__(self, key, value):
        self.parsed[key] = value

    @property
    def current_value(self):
        return self[self.current]

    def take_step(self):
        if self.current_value:
            self.turn(1)
        else:
            self.turn(-1)
        self[self.current] = not self.current_value
        self.total += self.current_value
        self.move()

    def part_a(self, iters=10_000):
        for _ in range(iters):
            self.take_step()
        # print(self.total)
        # return
        return self.total


if __name__ == "__main__":
    submit_answers(Solution, 22, 2017)