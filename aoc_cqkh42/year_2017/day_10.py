import itertools
from typing import Self, Any

import more_itertools
import numpy as np

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers

from functools import reduce
from operator import xor


def ordify_sequence(sequence):
    return [ord(i) for i in sequence] + [17, 31, 73, 47, 23]

def reduce_xor(sequence):
    return reduce(xor, sequence)

class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        ...

    def do_twist(self, rope, length, position):
        based_at_position = np.roll(rope, -position)[:length][::-1]
        if position + length <= len(rope):
            rope[position:position + length] = based_at_position[:length]
        # return rope
        else:
            a = len(rope[position:])
            rope[position:] = based_at_position[:a]
            rope[:length-a] = based_at_position[a:]
        return rope

    def do_run(self, rope, numbers, position=0, skip_size=0):
        for length in numbers:
            self.do_twist(rope, length, position)
            position += length + skip_size
            position %= len(rope)
            skip_size += 1
        return rope, position, skip_size

    def part_a(self, size=256):
        rope = np.ones(size).cumsum() -1
        rope, *_ = self.do_run(rope, self.numbers)
        return int(rope[0] * rope[1])


    def part_b(self):
        numbers = ordify_sequence(self.input_)
        rope = list(range(256))
        position = 0
        skip_size=0
        for _ in range(64):
            rope, position, skip_size = self.do_run(rope, numbers, position, skip_size)
        chunks = more_itertools.chunked(rope, 16)
        chunks=[reduce_xor(chunk) for chunk in chunks]
        chunks = [f'{i:x}' for i in chunks]
        chunks = [f'{i:0>2}' for i in chunks]
        return ''.join(chunks)


if __name__ == "__main__":
    submit_answers(Solution, 10, 2017)