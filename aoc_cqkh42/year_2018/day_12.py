from typing import Self, Any

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Solution(BaseSolution):
    state = ""
    valid = set()
    offset = 0
    def _parse(self: Self) -> Any:
        state, _, *rules = self.lines
        self.state = state.strip("initial state: ")
        self.state = tuple(char == "#" for char in self.state)
        split = (rule.split(" => ") for rule in rules)
        valid = (left for left, right in split if right == "#")
        self.valid = {tuple(char == "#" for char in rule) for rule in valid}
        new_state = tuple(more_itertools.strip(self.state, lambda x: not x))
        self.offset = len(new_state) - len(self.state)
        self.state = new_state

    def turn(self):
        self.state = (False, False, False, False, *self.state, False, False, False)
        self.state   = tuple(phrase in self.valid for phrase in more_itertools.windowed(self.state, 5, fillvalue=False))
        self.state = tuple(more_itertools.rstrip(self.state, lambda x: not x))
        while not self.state[0]:
            self.offset -= 1
            self.state = tuple(self.state[1:])

        self.offset += 2
    def part_a(self):
        for _ in range(20):
            self.turn()
        return sum(index for index, value in enumerate(self.state, -self.offset) if value)

    def part_b(self):
        answers = []
        for index in range(21, 201):
            self.turn()
            total = sum(index for index, value in enumerate(self.state, -self.offset) if value)
            answers.append(total)
        thousand = answers[-1]
        nines = answers[-2]
        step = thousand - nines
        start = thousand - (step *200)
        return (step*50_000_000_000) + start

if __name__ == "__main__":
    submit_answers(Solution, 12, 2018)
