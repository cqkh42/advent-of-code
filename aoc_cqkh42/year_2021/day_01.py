from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self):
        return [int(num) for num in self.lines]

    def part_a(self):
        return sum(
            second > line
            for (line, second) in zip(self.parsed, self.parsed[1:])
        )

    def part_b(self):
        windows = [
            sum(self.parsed[start:start + 3])
            for start in range(len(self.lines))
        ]
        return sum(
            second > line for (line, second) in zip(windows, windows[1:])
        )
