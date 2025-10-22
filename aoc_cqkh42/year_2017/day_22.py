import itertools
from collections import defaultdict
from string import ascii_uppercase
from typing import Self, Any

import networkx as nx

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

#todo coords
#todo grid
class Solution(BaseSolution):
    direction = 'N'
    current = (0, 0)
    total_a = 0
    total_b = 0

    def _reset_to_centre(self):
        x = (self.num_lines - 1) // 2
        self.current = (x, x)
        self.direction = "N"


    def _parse(self: Self) -> Any:
        d = set()
        for y_index, line in enumerate(self.lines):
            for x_index, value in enumerate(line):
                if value == "#":
                    d.add((x_index, y_index))
        return d

    def turn(self, change):
        v = ['N', 'E', 'S', 'W']
        current = v.index(self.direction)
        new = current + change
        self.direction = v[new % len(v)]

    def move(self):
        x, y = self.current
        turns = {"N": (x, y-1), "E": (x+1, y), "S": (x, y+1), "W": (x-1, y)}
        self.current = turns[self.direction]


    def __getitem__(self, item):
        return self.parsed[item]

    def __setitem__(self, key, value):
        self.parsed[key] = value

    @property
    def current_value(self):
        return self[self.current]

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
        total = 0
        self._reset_to_centre()
        infected = self.parsed.copy()
        for _ in range(iters):
            if self.current in infected:
                self.turn(1)
                infected.remove(self.current)
            else:
                self.turn(-1)
                infected.add(self.current)
                total += 1
            self.move()
        return total

    def part_b(self, iters=10_000_000):
        self._reset_to_centre()
        total = 0
        states = defaultdict(int, {location: 2 for location in self._parse()})
        for _ in range(iters):
            current_state = states.get(self.current, 0)
            total += current_state == 1
            self.turn(current_state - 1)
            states[self.current] =(current_state + 1) % 4
            self.move()
        return total

if __name__ == "__main__":
    submit_answers(Solution, 22, 2017)