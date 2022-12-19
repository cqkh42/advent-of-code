from aoc_cqkh42 import BaseSolution

from dataclasses import dataclass

import json
import math
import more_itertools


@dataclass
class Packet:
    packet: str

    def __post_init__(self):
        self.packet = json.loads(self.packet)

    def __lt__(self, other):
        return compare(self.packet, other.packet)

    def __eq__(self, other):
        if isinstance(other, list):
            return self.packet == other


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            result = compare(a, b)
            if result is not None:
                return result
        if len(left) == len(right):
            return None
        return len(left) < len(right)


class Solution(BaseSolution):
    def parse_data(self):
        pairs = self.data.split('\n\n')
        pairs = (pair.split('\n') for pair in pairs)
        pairs = [(Packet(left), Packet(right)) for left, right in pairs]
        return pairs

    def part_a(self):
        return sum(
            index
            for index, (left, right) in enumerate(self.parsed_data, start=1)
            if left < right
        )

    def part_b(self):
        packets = sorted((
            *more_itertools.flatten(self.parsed_data),
            Packet('[[2]]'),
            Packet('[[6]]')
        ))
        return math.prod(
            index
            for index, packet in enumerate(packets, start=1)
            if packet in ([[2]], [[6]])
        )
