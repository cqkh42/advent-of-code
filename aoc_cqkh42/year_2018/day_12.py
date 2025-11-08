from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Solution(BaseSolution):
    state = ""
    rules = {}
    def _parse(self: Self) -> Any:
        state, _, *rules = self.lines
        self.state = state.strip("initial state: ")
        for rule in rules:
            left, right = rule.split(" => ")
            self.rules[left] = right

    def turn(self):
        self.state = f"....{self.state}...."
        new_state = ""
        for index in range(len(self.state)):
            sub = self.state[index:index+5]
            new_state+= self.rules.get(sub, ".")
        self.state = new_state
    def part_a(self):
        for _ in range(20):
            self.turn()
        return sum(index for index, value in enumerate(self.state, -40) if value == "#")

        return

    def part_b(self):
        return

if __name__ == "__main__":
    submit_answers(Solution, 12, 2018)
