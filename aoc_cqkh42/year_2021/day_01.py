from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        return [int(num) for num in self.lines]

    def part_a(self):
        return sum(
            second > line
            for (line, second) in zip(self.parsed_data, self.parsed_data[1:])
        )

    def part_b(self):
        windows = [
            sum(self.parsed_data[start:start+3])
            for start in range(len(self.lines))
        ]
        return sum(
            second > line for (line, second) in zip(windows, windows[1:])
        )
