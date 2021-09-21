# TODO use parse?
from aoc_cqkh42 import BaseSolution


def iteration(instruction, reg, index):
    incr = 1
    instr, key, *_ = instruction
    if instr == 'jio' and reg[key] == 1:
        incr = instruction[2]
    elif instr == 'jie' and not reg[key] % 2:
        incr = instruction[2]
    elif instr == 'jmp':
        incr = int(key)
    elif instr == "inc":
        reg[key] += 1
    elif instr == 'tpl':
        reg[key] *= 3
    elif instr == 'hlf':
        reg[key] *= 0.5

    return reg, index + incr


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
        return self.run(registers)

    def part_b(self):
        registers = {'a': 1, 'b': 0}
        return self.run(registers)

    def run(self, registers):
        index = 0
        while True:
            try:
                instr = self.parsed_data[index]
                registers, index = iteration(instr, registers, index)
            except IndexError:
                return registers['b']



