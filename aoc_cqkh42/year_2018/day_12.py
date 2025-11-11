from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Solution(BaseSolution):
    state = ""
    rules = {}
    valid = set()
    offset = 0
    def _parse(self: Self) -> Any:
        state, _, *rules = self.lines
        self.state = state.strip("initial state: ")
        for rule in rules:
            left, right = rule.split(" => ")
            self.rules[left] = right
            if right == "#":
                self.valid.add(left)
        new_state = self.state.strip(".")
        self.offset = len(new_state) - len(self.state)
        self.state = new_state

    def turn(self):
        self.state = f"....{self.state}...."
        new_state = ""
        for index in range(len(self.state)):
            sub = self.state[index:index+5]
            if sub in self.valid:
                new_state += "#"
            else:
                new_state += "."
        self.state = new_state
        self.state = self.state.rstrip(".")
        while self.state.startswith("."):
            self.offset -= 1
            self.state = self.state[1:]

        self.offset += 2
    def part_a(self):
        for _ in range(20):
            self.turn()
        return sum(index for index, value in enumerate(self.state, -self.offset) if value == "#")

        return

    def part_b(self):
        return
        for index in range(50000000000):
            self.turn()
            if not index % 1_000:
                print(index, self.state)
        return sum(index for index, value in enumerate(self.state, -40) if value == "#")
        return

if __name__ == "__main__":
    submit_answers(Solution, 12, 2018)
