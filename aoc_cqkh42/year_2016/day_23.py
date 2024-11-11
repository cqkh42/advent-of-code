from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2016.day_12 import Computer


class Solution(BaseSolution):
    def part_a(self):
        c = Computer(self.input_)
        c.registers['a'] = 7
        c.run()
        return c.registers['a']

    def part_b(self):
        # return
        c = Computer(self.input_)
        c.registers['a'] = 12
        c.run()
        return c.registers['a']


if __name__ == "__main__":
    submit_answers(Solution, 23, 2016)