import itertools

import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution

# h = sum(y-(n-1))
# h = yn - sum(n) + n
# h = yn +n - n(n+1)/2)
# n(n+1)/2

y_min = -20
y_max = -10


def y_location(y, n):
    # TODO this could be cached and recursive?
    return int((y*n) + n - ((n*(n+1))/2))


def x_location(x, n):
    n = min(n, x)
    return y_location(x, n)


class Solution(BaseSolution):
    def _process_data(self):
        return parse.search(r'x={x_min:d}..{x_max:d}, y={y_min:d}..{y_max:d}',
                            self.input_)

    def part_a(self):
        v = abs(self.processed['y_min']) - 1
        return y_location(v, v)

    def part_b(self):
        y_min = self.processed['y_min']
        y_max = self.processed['y_max']

        x_min = self.processed['x_min']
        x_max = self.processed['x_max']
        # 3 columns for y
        # velocity, step, is_valid

        steps = range(1, 2 * abs(y_min) + 1)
        ys = (
            prod for prod in
            itertools.product(range(y_min, abs(y_min) + 2), steps)
            if y_min <= y_location(*prod) <= y_max
        )

        xs = (
            prod
            for prod in itertools.product(range(1, x_max+1), steps)
            if x_min <= x_location(*prod) <= x_max
        )

        answers = {
            (x_[0], y_[0]) for x_, y_ in itertools.product(xs, ys)
            if x_[1] == y_[1]
        }
        return len(answers)
