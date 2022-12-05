import json

from aoc_cqkh42 import BaseSolution


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
        data = [json.loads(self.data)]
        return recursive_sum(data)
