from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer


class Solution(BaseSolution):
    def part_a(self):
        computer = Computer(list(self.numbers), [1])
        computer.run()
        return computer.outputs.pop()

    def part_b(self):
        c = Computer(list(self.numbers), [5])
        c.run()
        return c.outputs.pop()
