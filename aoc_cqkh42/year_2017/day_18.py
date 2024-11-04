import functools
from dataclasses import dataclass, field
from typing import Self, Any

from collections import defaultdict

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

import more_itertools
import operator

func_map = {
    'set': lambda x, y: y,
    'add': lambda x, y: x+y,
    'mul': lambda x, y: x*y,
    'mod': lambda x, y: x%y,

    # ''
}

@dataclass
class Computer:
    instructions: list[str]
    index: 0 = 0
    registers: defaultdict = field(default_factory=lambda: defaultdict(int))
    played: list = field(default_factory=list)


    def __getitem__(self, item: str):
        if item.isalpha():
            return self.registers[item]
        return int(item)

    def __setitem__(self, key, value):
        self.registers[key] = value

    def run_line(self):
        command, *variables = self.instructions[self.index]
        step = 1
        if command == 'snd':
            v = variables[0]
            self.played.append(self[v])
        elif command == 'rcv':
            v = variables[0]
            if self[v]:
                return self.played[-1]

        elif command in {'set', 'add', 'mul', 'mod'}:
            x, y = variables
            self[x] = func_map[command](self[x], self[y])
        elif command == 'jgz':
            x, y = variables
            if self[x] > 0:
                step = self[y]
        self.index += step







class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        return [line.split() for line in self.lines]
    def part_a(self: Self) -> int:
        computer = Computer(self.processed)
        while True:
            result = computer.run_line()
            if result:
                return result
        print(computer.instructions)

    def part_b(self: Self):
        return



if __name__ == "__main__":
    submit_answers(Solution, 18, 2017)