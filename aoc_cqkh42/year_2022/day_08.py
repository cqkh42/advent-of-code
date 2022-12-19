import numpy as np

from aoc_cqkh42 import BaseSolution


# TODO needs a tidy, could do more with arrays

def visible(row):
    max_ = -1
    seen = []
    for item in row:
        seen.append(item > max_)
        max_ = max(max_, item)
    return seen


def visible_row(row):
    right = []
    for index in range(len(row)):
        terminating = [rem >= row[index] for rem in row[index + 1:]]
        if not terminating:
            right.append(0)
        elif sum(terminating):
            right.append(terminating.index(True) + 1)
        else:
            right.append(len(terminating))
    return right


class Solution(BaseSolution):
    def parse_data(self):
        forest = []
        for row in self.lines:
            r = [int(i) for i in row]
            forest.append(r)
        return forest

    def part_a(self):
        seen = np.zeros_like(self.parsed_data)
        for index, row in enumerate(self.parsed_data):
            from_left = visible(row)
            seen[index, from_left] = 1
            from_right = visible(row[::-1])[::-1]
            seen[index, from_right] = 1

        for index, col in enumerate(zip(*self.parsed_data)):
            from_top = visible(col)
            seen[from_top, index] = 1
            from_bottom = list(reversed(visible(col[::-1])))
            seen[from_bottom, index] = 1
        return seen.sum()

    def part_b(self):
        right = np.array([visible_row(row) for row in self.parsed_data])
        left = np.array(
            [visible_row(row[::-1])[::-1] for row in self.parsed_data])

        cols = [list(i) for i in zip(*self.parsed_data)]
        down = np.array([visible_row(row) for row in cols]).T
        up = np.array([visible_row(row[::-1])[::-1] for row in cols]).T
        i = (right * left * down * up)
        return i.max()
