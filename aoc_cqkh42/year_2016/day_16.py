from typing import Self, Any

import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


def dragon_curve(a, length):
    b = ~a[::-1]
    z =np.concatenate([a, [False], b])
    if len(a) * 2 + 1 < length:
        return dragon_curve(z, length)
    return z[:length]


def checksum(num):
    pairs = num.reshape(-1, 2)
    p = pairs[:, 0] == pairs[:, 1]
    if not len(p) % 2:
        return checksum(p)
    return ''.join(p.astype(int).astype(str))


class Solution(BaseSolution):
    def part_a(self):
        b = dragon_curve(self.parsed, 272)
        return checksum(b)

    def _parse(self: Self) -> Any:
        return np.array([int(num) for num in self.input_]).astype(bool)

    def part_b(self):
        b = dragon_curve(self.parsed, 35651584)
        return checksum(b)

if __name__ == "__main__":
    submit_answers(Solution, 16, 2016)