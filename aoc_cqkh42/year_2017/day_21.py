from typing import Self, Any

import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def create_thruple(lines):
    flipped = tuple(lines[::-1])
    rotate_right = tuple(''.join(i) for i in zip(*lines))
    rotate_left = tuple(''.join(reversed(line)) for line in rotate_right)
    return {tuple(lines), flipped, rotate_left, rotate_right}

def break_into_chunks(lines, chunksize):
    vertical_splits = more_itertools.chunked(lines, chunksize)
    for split in vertical_splits:
        a = list(zip(*split))
        for x in more_itertools.chunked(a, chunksize):
            y = list(zip(*x))
            yield tuple(''.join(i) for i in y)

def rebuild_into_chunks(lines, chunksize):
    ...



class Solution(BaseSolution):
    arr = ('.#.', '..#', '###')

    def _parse(self: Self) -> Any:
       print(self.parsed_lines)

    def _parse_line(self, line: str):
        left, right = line.split(' => ')
        right = right.split('/')
        left = left.split('/')
        return {arr: tuple(right) for arr in create_thruple(left)}

    def part_a(self, iterations):
        return

    def part_b(self):
        return


if __name__ == "__main__":
    submit_answers(Solution, 21, 2017)
