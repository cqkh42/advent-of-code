import itertools

from aoc_cqkh42 import BaseSolution

import more_itertools
import numpy as np
from pprint import pprint

def visible(row):
    max_ = -1
    seen = []
    for item in row:
        seen.append(item > max_)
        max_ = max(max_, item)
    return seen


def visible_row(row):
    right = []
    for index, i in enumerate(row):
        t = 0
        remainder = row[index+1:]
        # remainder = list(itertools.takewhile(lambda x: x <= i, remainder))
        # print(index, i, remainder)

        for ind, x in enumerate(remainder):
            if x < i:
                t+=1
            else:
                right.append(t+1)
                break
        else:
            right.append(t)
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
            from_right = list(reversed(visible(row[::-1])))
            seen[index, from_right] = 1

        for index, col in enumerate(zip(*self.parsed_data)):
            from_top = visible(col)
            seen[from_top, index] = 1
            from_bottom = list(reversed(visible(col[::-1])))
            seen[from_bottom, index] = 1
        return seen.sum()

    def part_b(self):
        right = np.array([visible_row(row) for row in self.parsed_data])
        left = np.array([visible_row(row[::-1])[::-1] for row in self.parsed_data])

        cols = [list(i) for i in zip(*self.parsed_data)]
        down = np.array([visible_row(row) for row in cols]).T
        up = np.array([visible_row(row[::-1])[::-1] for row in cols]).T
        i = (right * left * down * up)
        return i.max()

