from dataclasses import dataclass

from aoc_cqkh42.helpers.base_solution import BaseSolution


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
    def _process_data(self):
        instructions = [
            instr.replace(",", "").replace("+", "").split() for instr in
            self.lines
        ]
        instructions = [
            [part if part.isalpha() else int(part) for part in instr]
            for instr in instructions
        ]
        return instructions

    def part_a(self, target="b"):
        registers = {"a": 0, "b": 0}
        r = Register(registers, self.processed)
        r.run()
        return r.reg[target]

    def part_b(self, target="b"):
        registers = {"a": 1, "b": 0}
        r = Register(registers, self.processed)
        r.run()
        return r.reg[target]
