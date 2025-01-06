from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.year_2016.day_12 import Computer

#todo line words
#todo computer
class Solution(BaseSolution):
    def run(self, registers=None):
        registers = registers or {}
        computer = Computer(self.parsed_lines)
        computer.registers.update(registers)
        computer.run()
        return computer.registers['a']

    def _parse_line(self, line: str):
        return line.split()

    def part_a(self):
        return self.run({'a': 7})

    def part_b(self):
        return self.run({'a': 12})


if __name__ == "__main__":
    submit_answers(Solution, 23, 2016)
