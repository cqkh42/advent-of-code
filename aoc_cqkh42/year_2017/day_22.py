import itertools
from collections import defaultdict
from string import ascii_uppercase
from typing import Self, Any

import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Node:
    def __init__(self, string='.'):
        if string == '#':
            self.status_a = self.status_b ='infected'
        else:
            self.status_a = self.status_b = 'clean'

    def toggle_a(self):
        mapping = {'infected': 'clean'}
        self.status_a = mapping.get(self.status_a, 'infected')

    def toggle_b(self):
        mapping = {
            'clean': 'weakened',
            'weakened': 'infected',
            'infected': 'flagged',
            'flagged': 'clean'
        }
        self.status_b = mapping[self.status_b]

class Solution(BaseSolution):
    direction = 'N'
    current = (0, 0)
    total_a = 0
    total_b = 0

    def _parse(self: Self) -> Any:
        d = defaultdict(Node)
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                d[(x_index, y_index)] = Node(value)
                # if value == '#':
                #     d[(x_index, y_index)] = True
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

    def take_step_a(self):
        if self[self.current].status_a == 'infected':
            self.turn(1)
        else:
            self.turn(-1)
        self[self.current].toggle_a()
        self.total_a += self[self.current].status_a == 'infected'
        self.move()

    def take_step_b(self):
        if self[self.current].status_b == 'clean':
            self.turn(-1)
        elif self[self.current].status_b == 'infected':
            self.turn(1)
        elif self[self.current].status_b == 'flagged':
            self.turn(2)
        self[self.current].toggle_b()
        self.total_b += self[self.current].status_b == 'infected'
        self.move()

    def part_a(self, iters=10_000):
        for _ in range(iters):
            self.take_step_a()
        return self.total_a

    def part_b(self, iters=10_000_000):
        x = (len(self.lines) - 1) // 2
        self.current = (x, x)
        for _ in range(iters):
            self.take_step_b()
        return self.total_b

if __name__ == "__main__":
    submit_answers(Solution, 22, 2017)