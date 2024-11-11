from dataclasses import dataclass
from typing import Self, Any

import more_itertools
import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Particle:
    p: np.array
    v: np.array
    a: np.array

    def velocity_at(self, step):
        total = self.a * step
        return total + self.v

    def position_at(self, step):
        z = (self.a * (step+1))/2
        return step * (z + self.v) + self.p

    def distance_at(self, step):
        return np.abs(self.position_at(step)).sum().astype(int)


class Solution(BaseSolution):
    def _process_data(self: Self) -> Any:
        parser = parse.compile('{:d}')
        particles = []
        for line in self.lines:
            p = parser.findall(line)
            a = [i[0] for i in p]
            bits = [np.array(i) for i in more_itertools.chunked(a, 3)]
            particle = Particle(*bits)
            particles.append(particle)
        return particles

    def part_a(self):
        a = [particle.distance_at(1_000_000) for particle in self.processed]
        return np.argmin(a)

    def part_b(self):
        # print(self.processed)
        steps = []
        # try increasing this if it doesn't work
        for step in range(40):
            a = [particle.position_at(step) for particle in self.processed]
            vals, indices, counts = np.unique(a, return_counts=True, return_index=True, axis=0)
            single_counts = np.where(counts == 1)
            single_indices = set(indices[single_counts])
            steps.append(single_indices)
        return len(set.intersection(*steps))

if __name__ == "__main__":
    submit_answers(Solution, 20, 2017)