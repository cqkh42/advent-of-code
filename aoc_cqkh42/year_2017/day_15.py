from typing import Self, Any

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    a_outputs = []
    b_outputs = []

    def part_a(self):
        a, b = self.numbers
        mod = 2147483647
        a_factor_post_mod = 16807 % mod
        b_factor_post_mod = 48271 % mod
        total = 0
        for i in range(40_000_000):
            a = (a * a_factor_post_mod) % mod
            b = (b * b_factor_post_mod) % mod
            if a %65536 == b % 65536:
                print(a, b)
                total += 1
            if not a % 4:
                self.a_outputs.append(a)
            if not b % 8:
                self.b_outputs.append(b)
        return total

    def part_b(self):
        total = 0
        binned = (bin(a^b) for a, b in zip(self.a_outputs[:5_000_000], self.b_outputs[:5_000_000]))
        with_ending = (num.endswith('0'*16) for num in binned)
        return sum(with_ending)
        for a, b in zip(self.a_outputs[:5_000_000], self.b_outputs[:5_000_000]):
            if bin(a ^ b).endswith("0" * 16):
                total += 1
        return total


if __name__ == "__main__":
    submit_answers(Solution, 15, 2017)
