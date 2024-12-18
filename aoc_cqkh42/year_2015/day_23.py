from dataclasses import dataclass

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


#TODO computer style
@dataclass
class Register:
    reg: dict
    instructions: list
    index: int = 0

    def run(self):
        while True:
            try:
                self.iteration()
            except IndexError:
                return

    def iteration(self):
        incr = 1
        match self.instructions[self.index]:
            case ["jio", key, inc] if self.reg[key] == 1:
                incr = inc
            case ["jie", key, inc] if not self.reg[key] % 2:
                incr = inc
            case ["jmp", key]:
                incr = int(key)
            case ["inc", key]:
                self.reg[key] += 1
            case ["tpl", key]:
                self.reg[key] *= 3
            case ["hlf", key]:
                self.reg[key] *= 0.5
        self.index += incr


class Solution(BaseSolution):
    def _parse_line(self, line: str):
        replaced = line.replace(",", "").replace("+", "").split()
        return tuple(part if part.isalpha() else int(part) for part in replaced)

    def part_a(self, target="b"):
        registers = {"a": 0, "b": 0}
        r = Register(registers, self.parsed_lines)
        r.run()
        return r.reg[target]

    def part_b(self, target="b"):
        registers = {"a": 1, "b": 0}
        r = Register(registers, self.parsed_lines)
        r.run()
        return r.reg[target]


if __name__ == "__main__":
    submit_answers(Solution, 23, 2015)
