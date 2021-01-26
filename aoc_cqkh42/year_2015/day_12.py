import json
import re

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    regex = re.compile(r'-?\d+')

    def part_a(self):
        numbers = self.regex.findall(self.data)
        return sum(int(num) for num in numbers)

    def part_b(self):
        data = [json.loads(self.data)]

        answer = 0

        for item in data:
            if isinstance(item, int):
                answer += item
            elif isinstance(item, list):
                data.extend(item)
            elif isinstance(item, dict) and 'red' not in item.values():
                data.extend(item.values())
        return answer
