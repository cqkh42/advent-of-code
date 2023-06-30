import json
from typing import Self

from aoc_cqkh42.helpers.base_solution import BaseSolution


def recursive_sum(data):
    match data:
        case int(data):
            return data
        case list(data):
            return sum(recursive_sum(i) for i in data)
        case dict(data) if "red" not in data.values():
            a = (recursive_sum(i) for i in data.values())
            return sum(a)
        case _:
            return 0


class Solution(BaseSolution):
    def part_a(self):
        return sum(self.numbers)

    def part_b(self):
        data = [json.loads(self.input_)]
        return recursive_sum(data)

    def _process_data(self: Self) -> str:
        return self.input_
