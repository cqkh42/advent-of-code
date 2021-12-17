from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        depth = 0
        horizontal = 0
        for line in self.lines:
            match line.split():
                case ['forward', num]:
                    horizontal += int(num)
                case ['down', num]:
                    depth += int(num)
                case ['up', num]:
                    depth -= int(num)
        return depth * horizontal

    def part_b(self):
        depth = 0
        horizontal = 0
        aim = 0
        for line in self.lines:
            match line.split():
                case ['forward', num]:
                    horizontal += int(num)
                    depth += (aim * int(num))
                case ['down', num]:
                    aim += int(num)
                case ['up', num]:
                    aim -= int(num)
        return depth * horizontal