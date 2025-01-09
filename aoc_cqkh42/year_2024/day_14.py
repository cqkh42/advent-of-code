import itertools

import more_itertools

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def safety_factor(self, seconds):
        locations = [((x + (x_v * seconds)) % 101, (y + (y_v * seconds)) % 103) for
                     x, y, x_v, y_v in self.line_numbers]
        tl = sum(x < 50 and y < 51 for x, y in locations)
        bl = sum(x < 50 and y > 51 for x, y in locations)
        tr = sum(x > 50 and y < 51 for x, y in locations)
        br = sum(x > 50 and y > 51 for x, y in locations)
        return tl * tr * br * bl
    def part_a(self):
        return self.safety_factor(100)

    def part_b(self):
        #uses a hack I found that the christmas tree occurs when the safety factor is minimised
        return min(range(10_000), key=lambda x: self.safety_factor(x))

if __name__ == "__main__":
    submit_answers(Solution,14, 2024)
