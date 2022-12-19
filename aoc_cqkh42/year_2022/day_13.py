from aoc_cqkh42 import BaseSolution

from dataclasses import dataclass

import json


@dataclass
class Packet:
    def __init__(self, string):
        self.packet = json.loads(string)


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        return compare(left, right)
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        return compare(left, right)

    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            if compare(a, b) is not None:
                return compare(a, b)
        if len(left) == len(right):
            return None
        return len(left) < len(right)


class Solution(BaseSolution):
    def part_a(self):
        total = 0
        for index, pair in enumerate(self.data.split('\n\n'), start=1):
            a, b = pair.split('\n')
            a = list(json.loads(a))
            b = list(json.loads(b))
            result = compare(a, b)
            total += result * index
        return total

    def part_b(self):
        ...
