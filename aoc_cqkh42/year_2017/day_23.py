from operator import mul, sub

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

func_map = {
    "mul": mul,
    "sub": sub,
    "set": lambda x, y: y
}

#todo computer
class Program:
    def __init__(self, instructions):
        self.instructions = instructions
        self.index = 0
        self.registers = {key: 0 for key in 'abcdefgh'}
        self.history = []

    def __getitem__(self, item: str):
        if item.isalpha():
            return self.registers[item]
        return int(item)

    def __setitem__(self, key, value):
        self.registers[key] = value

    def run_line(self):
        command, x,y = self.instructions[self.index]
        self.history.append(command)
        step = 1
        if command in {"mul", "sub", "set"}:
            self[x] = func_map[command](self[x], self[y])
        elif command == "jnz" and self[x] != 0:
            step = self[y]
        self.index += step


class Solution(BaseSolution):
    def _parse_line(self, line: str):
        return line.split()

    def part_a(self) -> int:
        computer = Program(self.parsed_lines)
        while True:
            try:
                computer.run_line()
            except IndexError:
                return computer.history.count('mul')

    def optimise_program(self):
        a = list(self.parsed_lines)



    def part_b(self):
        computer = Program(self.parsed_lines)
        computer['a'] = 1
        for i in range(10_000_000):
            try:
                print(computer.index)
                computer.run_line()
            except IndexError:
                return computer['h']


if __name__ == "__main__":
    submit_answers(Solution,23, 2017)
