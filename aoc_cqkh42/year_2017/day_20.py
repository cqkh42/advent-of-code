import more_itertools
import numpy as np
import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

#todo coords
# @dataclass
class Particle:
    PARSER = parse.compile("{:d}")
    def __init__(self, data):
        numbers = [num[0] for num in self.PARSER.findall(data)]
        p, v, a = more_itertools.chunked(numbers, 3)
        self.p = np.array(p)
        self.v = np.array(v)
        self.a = np.array(a)

    def velocity_at(self, step):
        total = self.a * step
        return total + self.v

    def position_at(self, step):
        z = (self.a * (step + 1)) / 2
        return step * (z + self.v) + self.p

    def distance_at(self, step):
        return np.abs(self.position_at(step)).sum().astype(int)


class Solution(BaseSolution):
    def part_a(self):
        a = [particle.distance_at(1_000_000) for particle in self.lines_as(Particle)]
        return np.argmin(a)

    def part_b(self):
        particles = self.lines_as(Particle)
        steps = []
        # try increasing this if it doesn't work
        for step in range(40):
            a = [particle.position_at(step) for particle in particles]
            vals, indices, counts = np.unique(
                a, return_counts=True, return_index=True, axis=0
            )
            single_counts = np.where(counts == 1)
            single_indices = set(indices[single_counts])
            steps.append(single_indices)
        return len(set.intersection(*steps))


if __name__ == "__main__":
    submit_answers(Solution, 20, 2017)
