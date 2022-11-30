from dataclasses import dataclass
from typing import Dict, List

from aoc_cqkh42 import BaseSolution


@dataclass
class Computer:
    registers: Dict[str, int]
    instructions: List[str]
    index = 0

    def run(self):
        while self.index in range(len(self.instructions)):
            incr = 1
            match self.instructions[self.index]:
                case ['cpy', input_, target]:
                    val = self.registers.get(input_, input_)
                    self.registers[target] = int(val)
                case ['inc', input_]:
                    self.registers[input_] += 1
                case ['dec', input_]:
                    self.registers[input_] -= 1
                case ['jnz', input_, v]:
                    if self.registers.get(input_, input_):
                        incr = int(v)
                case ['tgl', x]:
                    self.toggle(x)
            self.index += incr
        return self.registers['a']

    def toggle(self, x):
        # if it is inc, it becomes dec, and vica versa



class Solution(BaseSolution):
    def parse_data(self):
        return [line.split() for line in self.lines]

    def part_a(self):
        registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        computer = Computer(registers, self.parsed_data)
        return computer.run()

    def part_b(self):
        registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        computer = Computer(registers, self.parsed_data)
        return computer.run()
