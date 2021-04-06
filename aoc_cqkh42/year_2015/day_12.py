import json

import parse

from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        hits = parse.findall(r'{num:d}', self.data)
        return sum(num['num'] for num in hits)

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
