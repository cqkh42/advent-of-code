from typing import Self, Any

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42 import submit_answers
import parse

class Solution(BaseSolution):
    a_outputs = []
    b_outputs = []
    def _process_data(self: Self) -> Any:
        a, b = parse.findall('{:d}', self.input_)
        return a[0], b[0]

    def part_a(self):
        a, b = self.processed
        mod = 2147483647
        a_factor_post_mod = 16807 % mod
        b_factor_post_mod = 48271 % mod
        total = 0
        for i in range(40_000_000):
            a = (a *a_factor_post_mod) % mod
            b = (b *b_factor_post_mod) % mod
            if bin(a^b).endswith('0'*16):
                total += 1
            if not a % 4:
                self.a_outputs.append(a)
            if not b % 8:
                self.b_outputs.append(b)
        return total

    def part_b(self):
        total = 0
        for a, b in zip(self.a_outputs[:5_000_000], self.b_outputs[:5_000_000]):
            if bin(a^b).endswith('0'*16):
                total += 1
        return total


if __name__ == "__main__":
    submit_answers(Solution, 15, 2017)