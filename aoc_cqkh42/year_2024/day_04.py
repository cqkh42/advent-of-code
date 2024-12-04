import itertools

import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def count(line):
    if isinstance(line, str):
        return line.count('XMAS') + line.count('SAMX')
    else:
        return count(''.join(line))


class Solution(BaseSolution):
    def part_a(self):
        arr = np.array([list(line) for line in self.lines])
        flipped = np.fliplr(arr)
        l_r = sum(count(line) for line in self.lines)
        t_b = sum(count(line) for line in zip(*self.lines))

        total = l_r + t_b
        total += sum(count(np.diag(arr, i)) for i in range(-self.num_lines, self.num_lines))
        total += sum(count(np.diag(flipped, i)) for i in range(-self.num_lines, self.num_lines))

        return total

    def is_l_r_mas(self, x, y):
        return (self.lines[y][x] + self.lines[y+1][x+1] + self.lines[y+2][x+2]
                in {'MAS', 'SAM'}
        )

    def is_r_l_mas(self, x, y):
        return (self.lines[y][x+2]+ self.lines[y+1][x+1] + self.lines[y+2][x]
                in {'MAS', 'SAM'}
        )

    def is_x_mas(self, coords):
        try:
            return self.is_l_r_mas(*coords) and self.is_r_l_mas(*coords)
        except IndexError:
            return False

    def part_b(self):
        p = itertools.product(range(len(self.lines[0])), repeat=2)
        return sum(self.is_x_mas(coords) for coords in p)


if __name__ == "__main__":
    submit_answers(Solution,4, 2024)
