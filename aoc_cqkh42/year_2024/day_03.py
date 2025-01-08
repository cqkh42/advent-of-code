import re
from typing import Self, Any

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def calc_mul(instructions):
    string = ''.join(instructions)
    pairs = parse.findall(r'mul({:d},{:d})', string)
    return sum(x * y for x, y in pairs)


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        return re.findall(r"(mul\(\d+,\d+\)|don't|do)", self.input_)

    def part_a(self):
        return calc_mul(self.parsed)

    def part_b(self):
        valid = []
        current_state = 'do'
        for instruction in self.parsed:
            if instruction in ("don't", 'do'):
                current_state = instruction
            elif current_state == 'do':
                valid.append(instruction)
        return calc_mul(valid)


if __name__ == "__main__":
    submit_answers(Solution,3, 2024)
