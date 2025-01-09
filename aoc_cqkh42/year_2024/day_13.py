from typing import Self, Any

import more_itertools
import numpy as np
import sympy

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        chunks = more_itertools.chunked(self.line_numbers, 3)
        out = []
        for x in chunks:
            z = zip(*x)
            out.append(list(list(z)))
            # print(list(z))
        return out
        return [(np.array([a, b]).T, np.array(c)) for a, b, c in chunks]

    def part_a(self):
        a, b = sympy.symbols("a, b", integer=True)
        total = 0
        for (x_a, x_b, x_c), (y_a, y_b,y_c) in self.parsed:
            s = sympy.solve([x_a*a + x_b*b - x_c, y_a*a + y_b*b - y_c], a, b)
            if s:
                total += s[a] * 3
                total += s[b]
        return total

    def part_b(self):
        num = 10000000000000

        a, b = sympy.symbols("a, b", integer=True)
        total = 0
        for (x_a, x_b, x_c), (y_a, y_b,y_c) in self.parsed:
            s = sympy.solve([x_a*a + x_b*b - (x_c+num), y_a*a + y_b*b - (y_c+num)], a, b)
            if s:
                total += s[a] * 3
                total += s[b]
        return total


if __name__ == "__main__":
    submit_answers(Solution,13, 2024)
