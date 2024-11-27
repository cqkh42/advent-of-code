from typing import Self, Any
from collections import ChainMap

import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

def _create_thruple(lines):
    arr = np.array([list(line) for line in lines])
    for i in range(4):
        rot = np.rot90(arr, i)
        yield rot
        yield np.flipud(rot)
        yield np.fliplr(rot)


def create_thruple(lines):
    return {
        tuple(''.join(i) for i in l) for l in _create_thruple(lines)
    }
    return set(list(_create_thruple(lines)))
    arr =np.array([list(line) for line in lines])
    rotate_one = tuple(''.join(i) for i in np.rot90(arr, 1).tolist())
    rotate_two = tuple(''.join(i) for i in np.rot90(arr, 2).tolist())
    rotate_three = tuple(''.join(i) for i in np.rot90(arr, 3).tolist())
    return {tuple(lines), flipped_v, flipped_h , rotate_one, rotate_two, rotate_three}

def break_into_chunks(lines):
    if not (len(lines) % 2):
        chunksize = 2
    else:
        chunksize = 3
    out = []
    vertical_splits = more_itertools.chunked(lines, chunksize)
    for split in vertical_splits:
        a = list(zip(*split))
        for x in more_itertools.chunked(a, chunksize):
            y = list(zip(*x))
            out.append(tuple(''.join(i) for i in y))
    return tuple(out)

def rebuild_into_lines(chunks):
    # if len(chunks) % 3:
    chunksize = int(len(chunks) **0.5)
        # break it into 4s
    # else:
    #     chunksize = len(chunks) // 3
        # break it into 3s
    # print(chunksize)
    a = list(more_itertools.chunked(chunks, chunksize))
    # print(a[1])
    out = []
    for piece in a:
        x = list(zip(*piece))
        for i in x:
            z = ''.join(i)
            out.append(z)
    return tuple(out)
    # print(list(a))

# .#.
# ..#
# ###

def counted(lines):
    total = 0
    for line in lines:
        total += line.count('#')
    return total

class Solution(BaseSolution):
    arr = ('.#.', '..#', '###')

    def _parse(self: Self) -> Any:
        d =  dict(ChainMap(*self.parsed_lines))
        # print(('.##', '#.#', '..#') in d)
        return d

    def _parse_line(self, line: str):
        left, right = line.split(' => ')
        right = right.split('/')
        left = left.split('/')
        return {arr: tuple(right) for arr in create_thruple(left)}

    def do_iteration(self):
        chunks = break_into_chunks(self.arr)
        mapped = tuple([self.parsed[chunk] for chunk in chunks])
        self.arr = rebuild_into_lines(mapped)

    def part_a(self, iterations=5):
        for i in range(iterations):
            # print(i)
            self.do_iteration()
        total = 0
        for line in self.arr:
            total += line.count('#')
        return total

    def part_b(self):
        for i in range(13):
            self.do_iteration()
        total = 0
        for line in self.arr:
            total += line.count('#')
        return total


if __name__ == "__main__":
    submit_answers(Solution, 21, 2017)
