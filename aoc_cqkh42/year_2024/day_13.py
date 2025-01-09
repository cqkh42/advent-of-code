import itertools
from typing import Self, Any

import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _parse(self: Self) -> Any:
        chunks = more_itertools.chunked(self.line_numbers, 3)
        return [(np.array([a, b]).T, np.array(c)) for a, b, c in chunks]

    def part_a(self):
        solutions = (np.linalg.inv(arr).dot(c) for arr, c in self.parsed)
        solutions = (s for s in solutions if np.all(np.isclose(s, s.round())))
        solutions = ((solution * [3,1]).sum() for solution in solutions)
        return int(sum(solutions))

    def part_b(self):
        num = 10000000000000
        solutions = (np.linalg.inv(arr).dot(c+num) for arr, c in self.parsed)
        solutions = (s for s in solutions if np.all(np.isclose(s, s.round())))
        solutions = ((solution * [3,1]).sum() for solution in solutions)
        return int(sum(solutions))
        # 1545093008502 is too high

        print()
        chunks = more_itertools.chunked(self.line_numbers, 3)
        total = 0
        for a, b, c in chunks:
            arr = np.array([a, b])
            c = np.array(c) + 10000000000000

            solution = np.linalg.inv(arr.T).dot(c)
            score = (solution * [3, 1]).sum().round()

            if np.all([np.isclose(num.round(0), num) for num in solution]):
                print(a, b, c, solution, solution.astype(str))
                total += score
        return int(total)


if __name__ == "__main__":
    submit_answers(Solution,13, 2024)
