from collections import defaultdict
from dataclasses import dataclass
from typing import Self, Any

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

func_map = {
    "set": lambda x, y: y,
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
    "mod": lambda x, y: x % y,
    # ''
}


class BaseProgram:
    def __init__(self, instructions):
        self.instructions = instructions
        self.index = 0
        self.registers = defaultdict(int)
        self.outputs = []
        self.inputs_ = []
        self.awaiting_input: bool = False
        self.output_count: int = 0

    def __getitem__(self, item: str):
        if item.isalpha():
            return self.registers[item]
        return int(item)

    def __setitem__(self, key, value):
        self.registers[key] = value

    def snd(self, v):
        self.outputs.append(self[v])
        self.output_count += 1

    def run_line(self):
        command, *variables = self.instructions[self.index]
        step = 1
        if command == "snd":
            self.snd(variables[0])
        elif command == "rcv":
            step = self.rcv(variables[0])

        elif command in {"set", "add", "mul", "mod"}:
            x, y = variables
            self[x] = func_map[command](self[x], self[y])
        elif command == "jgz":
            x, y = variables
            if self[x] > 0:
                step = self[y]
        self.index += step


class ProgramA(BaseProgram):
    def __init__(self, instructions):
        super().__init__(instructions)

    def rcv(self, v):
        self.awaiting_input = bool(self[v])
        return 1


@dataclass
class ProgramB(BaseProgram):
    def __init__(self, instructions):
        super().__init__(instructions)

    def rcv(self, v):
        self.awaiting_input = not self.inputs_
        step = bool(self.inputs_)
        if self.inputs_:
            next_value = self.inputs_.pop(0)
            self[v] = next_value
        return step


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        return [line.split() for line in self.lines]

    def part_a(self: Self) -> int:
        computer = ProgramA(self.parsed)
        while True:
            computer.run_line()
            if computer.awaiting_input:
                return computer.outputs[-1]

    def part_b(self: Self):
        program_0 = ProgramB(self.parsed)
        program_0["p"] = 0

        program_1 = ProgramB(self.parsed)
        program_1["p"] = 1

        while (not program_0.awaiting_input) or (not program_1.awaiting_input):
            program_0.run_line()
            if program_0.outputs:
                program_1.inputs_.append(program_0.outputs.pop(0))
            program_1.run_line()
            if program_1.outputs:
                program_0.inputs_.append(program_1.outputs.pop(0))
        return program_1.output_count


if __name__ == "__main__":
    submit_answers(Solution, 18, 2017)
