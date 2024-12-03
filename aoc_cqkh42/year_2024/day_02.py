import itertools

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def remove_list_items(line):
    for index in range(len(line)):
        yield line[:index] + line[index+1:]


class Solution(BaseSolution):
    PARSER = parse.compile('{:d}')

    def _parse_line(self, line: str):
        return [result[0] for result in self.PARSER.findall(line)]

    def is_safe_line(self, line):
        line = list(itertools.pairwise(line))
        decreasing = all(x > y for x, y in line)
        increasing = all(y > x for x, y in line)
        in_range = all(abs(x - y) <= 3 for x, y in line)
        return bool(in_range and (decreasing or increasing))

    def part_a(self):
        return sum(self.is_safe_line(line) for line in self.parsed_lines)

    def could_be_safe_line(self, line):
        removals = (
            self.is_safe_line(option) for option in remove_list_items(line)
        )
        return self.is_safe_line(line) or any(removals)

    def part_b(self):
        return sum(self.could_be_safe_line(line) for line in self.parsed_lines)


if __name__ == "__main__":
    submit_answers(Solution,2, 2024)
