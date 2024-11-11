from typing import Self, Any

import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

class Mapper:
    def __init__(self, mappings):
        self.mappings = mappings

    def __getitem__(self, item):


def resample(arr, N):
    A = []
    for v in np.vsplit(arr, arr.shape[0] // N):
        A.extend([*np.hsplit(v, arr.shape[0] // N)])
    return np.array(A)

def do_three_iteration(start, mappings):
    for chunk in resample(start, 3):
        new_chunk = mappings[chunk]
        print(new_chunk)


class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
       ...

    def part_a(self, iterations):
        return

    def part_b(self):
        return


if __name__ == "__main__":
    submit_answers(Solution, 21, 2017)
