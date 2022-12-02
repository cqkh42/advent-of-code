from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        elves = self.data.split('\n\n')
        elves = [elf.split('\n') for elf in elves]
        elves = [sum(int(num) for num in elf) for elf in elves]
        return sorted(elves, reverse=True)

    def part_a(self):
        return self.parsed_data[0]

    def part_b(self):
        return sum(self.parsed_data[:3])
