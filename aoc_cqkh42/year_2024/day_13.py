import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_a(self):
        print()
        chunks = more_itertools.chunked(self.line_numbers, 3)
        total = 0
        for a, b, c in chunks:
            arr = np.array([a, b])
            solution = np.linalg.inv(arr.T).dot(c)
            print(a, b, c, solution)
            if all([np.isclose(num%1, 0) for num in solution]):

                total += (solution * [3,1]).sum()
        return int(total)



    def part_b(self):
        ...


if __name__ == "__main__":
    submit_answers(Solution,13, 2024)
