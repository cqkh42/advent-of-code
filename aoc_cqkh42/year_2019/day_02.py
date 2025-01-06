import itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2019.computer import Computer

#todo computer
class Solution(BaseSolution):
    def part_a(self):
        intcode = list(self.numbers)
        intcode[1] = 12
        intcode[2] = 2
        computer = Computer(intcode)
        computer.run()
        return computer.intcode[0]

    def part_b(self):
        for noun, verb in itertools.product(range(100), range(100)):
            intcode = list(self.numbers)
            intcode[1] = noun
            intcode[2] = verb
            computer = Computer(intcode)
            computer.run()
            if computer.intcode[0] == 19690720:
                return 100 * noun + verb
