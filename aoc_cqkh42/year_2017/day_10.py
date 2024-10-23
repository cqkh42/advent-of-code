import itertools
from typing import Self, Any

import more_itertools
import numpy as np

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

from functools import reduce
from operator import xor


class KnotHash:
    def __init__(self, numbers, iterations=64, ordify=True):
        self.rope = list(range(256))
        self.position = 0
        self.skip_size = 0
        self.iterations = iterations
        if ordify:
            self.numbers = ordify_sequence(numbers)
        else:
            self.numbers = numbers

    def do_twist(self, length):
        based_at_position = np.roll(self.rope, -self.position)[:length][::-1]
        if self.position + length <= len(self.rope):
            self.rope[self.position:self.position + length] = based_at_position[:length]
        else:
            a = len(self.rope[self.position:])
            self.rope[self.position:] = based_at_position[:a]
            self.rope[:length - a] = based_at_position[a:]
        return self.rope

    def do_run(self):
        for length in self.numbers:
            self.do_twist(length)
            self.position += length + self.skip_size
            self.position %= len(self.rope)
            self.skip_size += 1
        return self.rope, self.position, self.skip_size

    def do_runs(self):
        for _ in range(self.iterations):
            self.do_run()

    def make_hash(self):
        self.do_runs()
        chunks = more_itertools.chunked(self.rope, 16)
        chunks = [reduce_xor(chunk) for chunk in chunks]
        chunks = [f'{i:x}' for i in chunks]
        chunks = [f'{i:0>2}' for i in chunks]
        return ''.join(chunks)


def ordify_sequence(sequence):
    return [ord(i) for i in sequence] + [17, 31, 73, 47, 23]

def reduce_xor(sequence):
    return reduce(xor, sequence)


class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        ...

    def part_a(self, size=256):
        hasher = KnotHash(self.numbers, 1, ordify=False)
        hasher.make_hash()
        rope = hasher.rope
        return int(rope[0] * rope[1])

    def part_b(self):
        hasher = KnotHash(self.input_)
        return hasher.make_hash()


if __name__ == "__main__":
    submit_answers(Solution, 10, 2017)