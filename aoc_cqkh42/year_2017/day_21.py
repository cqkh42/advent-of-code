from typing import Self, Any
from collections import ChainMap, UserDict

import more_itertools
import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Mapper:
    def __init__(self, maps=None):
        self._map = {}
        if maps:
            for k, v in maps.items():
                self[k] = v


    def __getitem__(self, item):
        if isinstance(item, tuple):
            a = np.array([list(i) for i in item])
            return self._map[a.tobytes()]
        elif isinstance(item, np.array):
            return self._map[item.tobytes()]
        else:
            raise TypeError

    def __setitem__(self, key, value):
        self._map[key] = value

        arr = np.array([list(line) for line in key])
        for i in range(4):
            rot = np.rot90(arr, i)
            self._map[rot.tobytes()] = value
            self._map[np.flipud(rot).tobytes()] = value
            self._map[np.fliplr(rot).tobytes()] = value


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
    chunksize = int(len(chunks) **0.5)
    a = list(more_itertools.chunked(chunks, chunksize))
    out = []
    for piece in a:
        x = list(zip(*piece))
        for i in x:
            z = ''.join(i)
            out.append(z)
    return tuple(out)

def counted(lines):
    total = 0
    for line in lines:
        total += line.count('#')
    return total

class Solution(BaseSolution):
    arr = ('.#.', '..#', '###')

    def _parse(self: Self) -> Any:
        return Mapper(dict(self.parsed_lines))

    def _parse_line(self, line: str) -> tuple:
        left, right = line.split(' => ')
        right = right.split('/')
        left = left.split('/')
        return tuple(left), tuple(right)

    def do_iteration(self):
        print(self.parsed._map)
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
