import more_itertools

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        elves = more_itertools.split_at(self.lines, lambda line: line == '')
        elves = [sum(int(weight) for weight in elf) for elf in elves]
        return sorted(elves, reverse=True)

    def part_a(self):
        return self.parsed[0]

    def part_b(self):
        return sum(self.parsed[:3])
