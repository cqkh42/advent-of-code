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
class ProgramA:
    instructions: list[str]
    index: 0 = 0
    registers: defaultdict = field(default_factory=lambda: defaultdict(int))
    played: list = field(default_factory=list)
    has_received = False
    still_running = True
    just_sent = False
    queue = []


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
            self.just_sent = True
        elif command == 'rcv':
            v = variables[0]
            if self[v]:
                self.has_received = True

        elif command in {'set', 'add', 'mul', 'mod'}:
            x, y = variables
            self[x] = func_map[command](self[x], self[y])
        elif command == 'jgz':
            x, y = variables
            if self[x] > 0:
                step = self[y]
        self.index += step

@dataclass
class ProgramB:
    instructions: list[str]
    index: int = 0
    registers: defaultdict = field(default_factory=lambda: defaultdict(int))
    outputs: list = field(default_factory=list)
    inputs_: list = field(default_factory=list)
    awaiting_input: bool = False
    output_count: int = 0


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
            self.outputs.append(self[v])
            self.output_count += 1
        elif command == 'rcv':
            v = variables[0]
            if not self.inputs_:
                self.awaiting_input = True
                step = 0
            else:
                self.awaiting_input = False
                next_value = self.inputs_.pop(0)
                self[v] = next_value


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
        computer = ProgramA(self.processed)
        while True:
            computer.run_line()
            if computer.has_received:
                return computer.played[-1]

    def part_b(self: Self):
        # ...
        program_0 = ProgramB(self.processed)
        program_0['p'] = 0
        #
        program_1 = ProgramB(self.processed)
        program_1['p'] = 1

        while (not program_0.awaiting_input) or (not program_1.awaiting_input):
            program_0.run_line()
            if program_0.outputs:
                program_1.inputs_.append(program_0.outputs.pop(0))
            program_1.run_line()
            if program_1.outputs:
                program_0.inputs_.append(program_1.outputs.pop(0))
        return program_1.output_count



        #
        # while program_0.still_running or program_1.still_running:
        #     program_0.run_line()
        #     if program_0.just_sent:
        #         p = program_0.played.pop()
        #         program_1.queue.append(p)
        #         program_0.just_sent = False
        #     if program_0.





if __name__ == "__main__":
    submit_answers(Solution, 18, 2017)