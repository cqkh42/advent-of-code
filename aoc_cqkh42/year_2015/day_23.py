# TODO use parse?
from dataclasses import dataclass

from aoc_cqkh42 import BaseSolution


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
                return self.reg['b']

    def iteration(self):
        incr = 1
        match self.instructions[self.index]:
            case ['jio', key, inc] if self.reg[key] == 1:
                incr = inc
            case ['jie', key, inc] if not self.reg[key] % 2:
                incr = inc
            case ['jmp', key]:
                incr = int(key)
            case ['inc', key]:
                self.reg[key] += 1
            case ['tpl', key]:
                self.reg[key] *= 3
            case ['hlf', key]:
                self.reg[key] *= 0.5
        self.index += incr


class Solution(BaseSolution):
    def parse_data(self):
        instructions = self.data.split('\n')
        instructions = [
            instr.replace(',', '').replace('+', '').split()
            for instr in instructions]
        instructions = [
            [part if part.isalpha() else int(part) for part in instr]
            for instr in instructions
        ]
        return instructions

    def part_a(self):
        registers = {'a': 0, 'b': 0}
        r = Register(registers, self.parsed_data)
        return r.run()

    def part_b(self):
        registers = {'a': 1, 'b': 0}
        r = Register(registers, self.parsed_data)
        return r.run()
