from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self):
        return [int(num) for num in self.lines]

    def part_a(self):
        return sum(
            second > line
            for (line, second) in zip(self.processed, self.processed[1:])
        )

    def part_b(self):
        windows = [
            sum(self.processed[start:start + 3])
            for start in range(len(self.lines))
        ]
        return sum(
            second > line for (line, second) in zip(windows, windows[1:])
        )
