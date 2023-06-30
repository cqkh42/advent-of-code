from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer


class Solution(BaseSolution):
    def part_a(self):
        computer = Computer(list(self.numbers), [1])
        computer.run()
        return computer.output

    def part_b(self):
        computer = Computer(list(self.numbers), [2])
        computer.run()
        return computer.output
